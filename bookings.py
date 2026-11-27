from sessions import find_session


def show_seat_map(session):
    print(f"\nОрундар картасы ({session['movie_title']} - {session['time']}):")
    for r_idx, row in enumerate(session["booked"]):
        line = []
        for c_idx, is_taken in enumerate(row):
            seat_label = f"{r_idx + 1}-{c_idx + 1}"
            if is_taken:
                line.append(f"[{seat_label}:БАНД]")
            else:
                line.append(f"[{seat_label}:БОШ]")
        print(" ".join(line))


def book_ticket(sessions, bookings):
    if not sessions:
        print("Брондоого ылайык сеанс жок.")
        return

    try:
        session_id = int(input("Сеанстын ID номери: "))
        row_num = int(input("Катар номери: "))
        col_num = int(input("Орун номери: "))
    except ValueError:
        print("Ката: сан жазыңыз.")
        return

    session = find_session(sessions, session_id)
    if not session:
        print("Сеанс табылган жок.")
        return

    r_idx = row_num - 1
    c_idx = col_num - 1

    if r_idx < 0 or r_idx >= len(session["booked"]) or c_idx < 0 or c_idx >= len(session["booked"][0]):
        print("Ката: мындай орун жок.")
        return

    if session["booked"][r_idx][c_idx]:
        print("Бул орун мурунтан эле брондолгон.")
        return

    customer = input("Кардардын аты: ").strip()
    if not customer:
        customer = "Конок"

    session["booked"][r_idx][c_idx] = True
    booking_id = 1 if not bookings else max(item["id"] for item in bookings) + 1
    bookings.append({
        "id": booking_id,
        "session_id": session["id"],
        "customer": customer,
        "seat": f"{row_num}-{col_num}",
        "price": session["price"]
    })
    print(f"Билет брондолду! Брон ID: {booking_id}, Орун: {row_num}-{col_num}, Баасы: {session['price']}")


def cancel_booking(sessions, bookings):
    if not bookings:
        print("Активдүү брондор жок.")
        return

    try:
        booking_id = int(input("Жокко чыгарылуучу брондун ID номери: "))
    except ValueError:
        print("Ката: сан жазыңыз.")
        return

    target = None
    for b in bookings:
        if b["id"] == booking_id:
            target = b
            break

    if not target:
        print("Мындай брон табылган жок.")
        return

    session = find_session(sessions, target["session_id"])
    if session:
        parts = target["seat"].split("-")
        r_idx = int(parts[0]) - 1
        c_idx = int(parts[1]) - 1
        session["booked"][r_idx][c_idx] = False

    bookings.remove(target)
    print(f"Брон #{booking_id} жокко чыгарылды.")


def list_bookings(bookings):
    if not bookings:
        print("Брондордун тизмеси бош.")
        return

    print("\n--- Брондолгон билеттер ---")
    for b in bookings:
        print(f"Брон ID: {b['id']} | Сеанс ID: {b['session_id']} | Кардар: {b['customer']} | Орун: {b['seat']} | Баасы: {b['price']}")
