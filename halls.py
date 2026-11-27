def create_seats(rows, cols):
    seats = []
    for r in range(1, rows + 1):
        row_seats = []
        for c in range(1, cols + 1):
            row_seats.append(f"{r}-{c}")
        seats.append(row_seats)
    return seats


def add_hall(halls):
    name = input("Залдын аты: ").strip()
    if not name:
        print("Ката: залдын аты бош болбошу керек.")
        return

    try:
        rows = int(input("Катарлардын саны: "))
        cols = int(input("Ар катардагы орундардын саны: "))
        if rows <= 0 or cols <= 0:
            print("Ката: катар жана орун саны оң сан болушу керек.")
            return
    except ValueError:
        print("Ката: бүтүн сан жазыңыз.")
        return

    hall_id = 1 if not halls else max(item["id"] for item in halls) + 1
    halls.append({
        "id": hall_id,
        "name": name,
        "rows": rows,
        "cols": cols,
        "seats": create_seats(rows, cols)
    })
    print(f"'{name}' залы кошулду. Жалпы орун: {rows * cols}, ID: {hall_id}")


def list_halls(halls):
    if not halls:
        print("Залдардын тизмеси бош.")
        return

    print("\n--- Залдар ---")
    for hall in halls:
        total = hall["rows"] * hall["cols"]
        print(f"ID: {hall['id']} | {hall['name']} | {hall['rows']}x{hall['cols']} ({total} орун)")


def find_hall(halls, hall_id):
    for hall in halls:
        if hall["id"] == hall_id:
            return hall
    return None
