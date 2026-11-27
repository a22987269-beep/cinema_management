from movies import find_movie
from halls import find_hall


def create_session(sessions, movies, halls):
    if not movies:
        print("Алгач тасма кошуңуз.")
        return
    if not halls:
        print("Алгач зал кошуңуз.")
        return

    try:
        movie_id = int(input("Тасманын ID номери: "))
        hall_id = int(input("Залдын ID номери: "))
        price = float(input("Билеттин баасы: "))
        if price <= 0:
            print("Ката: баа нөлдөн жогору болушу керек.")
            return
    except ValueError:
        print("Ката: туура маани жазыңыз.")
        return

    movie = find_movie(movies, movie_id)
    if not movie:
        print("Тасма табылган жок.")
        return

    hall = find_hall(halls, hall_id)
    if not hall:
        print("Зал табылган жок.")
        return

    time_slot = input("Сеанс убактысы (мисалы 18:30): ").strip()
    if not time_slot:
        print("Ката: убакыт көрсөтүлүшү керек.")
        return

    booked = []
    for row in hall["seats"]:
        booked.append([False for _ in row])

    session_id = 1 if not sessions else max(item["id"] for item in sessions) + 1
    sessions.append({
        "id": session_id,
        "movie_id": movie["id"],
        "movie_title": movie["title"],
        "hall_id": hall["id"],
        "hall_name": hall["name"],
        "time": time_slot,
        "price": price,
        "booked": booked
    })
    print(f"Сеанс түзүлдү. ID: {session_id} | {movie['title']} ({time_slot})")


def list_sessions(sessions):
    if not sessions:
        print("Азырынча сеанстар жок.")
        return

    print("\n--- Сеанстар ---")
    for s in sessions:
        print(f"ID: {s['id']} | {s['movie_title']} | Зал: {s['hall_name']} | Убактысы: {s['time']} | Баасы: {s['price']}")


def find_session(sessions, session_id):
    for s in sessions:
        if s["id"] == session_id:
            return s
    return None
