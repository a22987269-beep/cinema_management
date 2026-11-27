from movies import add_movie, list_movies, delete_movie
from halls import add_hall, list_halls
from sessions import create_session, list_sessions, find_session
from bookings import show_seat_map, book_ticket, cancel_booking, list_bookings


def print_menu():
    print("\n=== КИНОТЕАТР СИСТЕМАСЫ ===")
    print("1. Тасма кошуу")
    print("2. Тасмаларды көрүү")
    print("3. Тасма өчүрүү")
    print("4. Зал кошуу")
    print("5. Залдарды көрүү")
    print("6. Сеанс түзүү")
    print("7. Сеанстарды көрүү")
    print("8. Орундар картасын көрүү")
    print("9. Билет брондоо")
    print("10. Брондолгон билеттерди көрүү")
    print("11. Бронду жокко чыгаруу")
    print("0. Чыгуу")


def main():
    movies = []
    halls = []
    sessions = []
    bookings = []

    while True:
        print_menu()
        choice = input("Тандооңузду жазыңыз: ").strip()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            list_movies(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            add_hall(halls)
        elif choice == "5":
            list_halls(halls)
        elif choice == "6":
            create_session(sessions, movies, halls)
        elif choice == "7":
            list_sessions(sessions)
        elif choice == "8":
            try:
                sid = int(input("Сеанстын ID номери: "))
                session = find_session(sessions, sid)
                if session:
                    show_seat_map(session)
                else:
                    print("Сеанс табылган жок.")
            except ValueError:
                print("Ката: сан жазыңыз.")
        elif choice == "9":
            book_ticket(sessions, bookings)
        elif choice == "10":
            list_bookings(bookings)
        elif choice == "11":
            cancel_booking(sessions, bookings)
        elif choice == "0":
            print("Программа токтотулду.")
            break
        else:
            print("Туура эмес тандоо. Кайра аракет кылыңыз.")


if __name__ == "__main__":
    main()
