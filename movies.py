

def add_movie(movies):
    title = input("Тасманын аты: ").strip()
    if not title:
        print("Ката: тасманын аты бош болбошу керек.")
        return

    genre = input("Жанры: ").strip()
    if not genre:
        genre = "Көрсөтүлгөн эмес"

    try:
        duration = int(input("Узактыгы (мүнөт менен): "))
        if duration <= 0:
            print("Ката: узактыгы нөлдөн чоң сан болушу керек.")
            return
    except ValueError:
        print("Ката: сан жазыңыз.")
        return

    movie_id = 1 if not movies else max(item["id"] for item in movies) + 1
    movies.append({
        "id": movie_id,
        "title": title,
        "genre": genre,
        "duration": duration
    })
    print(f"'{title}' тасмасы кошулду. ID: {movie_id}")


def list_movies(movies):
    if not movies:
        print("Тасмалардын тизмеси бош.")
        return

    print("\n--- Тасмалар ---")
    for movie in movies:
        print(f"ID: {movie['id']} | {movie['title']} | Жанр: {movie['genre']} | {movie['duration']} мүн.")


def find_movie(movies, movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def delete_movie(movies):
    if not movies:
        print("Өчүрө турган тасма жок.")
        return

    list_movies(movies)
    try:
        movie_id = int(input("Өчүрүлүүчү тасманын ID номерин жазыңыз: "))
    except ValueError:
        print("Ката: туура ID жазыңыз.")
        return

    movie = find_movie(movies, movie_id)
    if movie:
        movies.remove(movie)
        print(f"'{movie['title']}' өчүрүлдү.")
    else:
        print("Мындай ID менен тасма табылган жок.")
