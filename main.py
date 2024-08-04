class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.movie_counter = 1
        self.user_counter = 1
        self.ticket_counter = 1

    def addMovie(self, movieName):
        movie_id = self.movie_counter
        self.movies[movie_id] = movieName
        self.movie_counter += 1
        return movie_id

    def showAllMovies(self):
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def addUser(self, userName):
        user_id = self.user_counter
        self.users[user_id] = userName
        self.user_counter += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.ticket_counter
            self.tickets[ticket_id] = (userId, movieId)
            self.ticket_counter += 1
            return ticket_id
        return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        return False


def main():
    cinemaSystem = CinemaTicketSystem()

    while True:
        print("\nЗдравствуйте, у вас есть следующие доступные функции:")
        print("1. Добавить новый фильм")
        print("2. Показать все доступные фильмы")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("6. Выйти")
        
        choice = input("Выберите опцию (1-6): ")

        if choice == '1':
            movieName = input("Введите название фильма: ")
            movieId = cinemaSystem.addMovie(movieName)
            print(f"Фильм добавлен с идентификатором: {movieId}")

        elif choice == '2':
            print("Доступные фильмы:")
            cinemaSystem.showAllMovies()

        elif choice == '3':
            userName = input("Введите имя пользователя: ")
            userId = cinemaSystem.addUser(userName)
            print(f"Пользователь добавлен с идентификатором: {userId}")

        elif choice == '4':
            try:
                userId = int(input("Введите идентификатор пользователя: "))
                movieId = int(input("Введите идентификатор фильма: "))
                ticketId = cinemaSystem.buyTicket(userId, movieId)
                if ticketId:
                    print(f"Билет куплен с идентификатором: {ticketId}")
                else:
                    print("Ошибка: Неправильный идентификатор пользователя или фильма.")
            except ValueError:
                print("Ошибка: Введите числовые значения для идентификаторов.")

        elif choice == '5':
            try:
                ticketId = int(input("Введите идентификатор билета: "))
                if cinemaSystem.cancelTicket(ticketId):
                    print("Билет успешно отменен.")
                else:
                    print("Ошибка: Билет с таким идентификатором не найден.")
            except ValueError:
                print("Ошибка: Введите числовое значение для идентификатора билета.")

        elif choice == '6':
            print("Выход из системы.")
            break

        else:
            print("Ошибка: Неправильный выбор. Пожалуйста, выберите опцию от 1 до 6.")


if __name__ == "__main__":
    main()
