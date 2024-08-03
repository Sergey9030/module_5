from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname        # Имя пользователя
        self.password = hash(password)  # Пароль
        self.age = age                  # Возраст
    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title             # Заголовок видео
        self.duration = duration       # Продолжительность видео
        self.time_now = time_now       # Секунда остановки
        self.adult_mode = adult_mode   # Есть возрастные ограничения

    def __str__(self):
        return f'Название:{self.title}, Длительность:{self.duration}'

    def __eq__(self, other):
        return self.title == other


class UrTube:

    def __init__(self):
        self.videos = []            # Список видео
        self.users = []             # Список пользователей
        self.current_user = None    # Текущий пользователь

    def log_in(self, nickname, password):  # Ищет пользователя
        print(nickname)
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname and hash(self.users[i].password) == hash(password):
                self.current_user = self.users[i]
                return self.users[i]
        print('Такого пользователя не существует')
        return None

    def register(self, nickname, password, age):  # Регистрирует пользователя
        fnd = False
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return None
        self.users.append(User(nickname, password, age))
        self.current_user = self.users[len(self.users)-1]
        return self.current_user

    def log_out(self):  # Сброс пользователя (выход из аккаунта)
        self.current_user = None

    def add(self, *v):
        for i in v:
            self.videos.append(i)

    def get_videos(self, vp):
        fnd_list = []
        for i in range(len(self.videos)):
            if vp.upper() in self.videos[i].title.upper():
                fnd_list.append(self.videos[i].title)
        return fnd_list

    def watch_video(self, vn):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for v in self.videos:
            if v.title == vn:
                if v.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    for i in self.videos:
                        if i == vn:
                            print(f'{i}:')
                            for t in range(i.duration):
                                print(f'{t+1} ', end='')
                                sleep(1)
                                i.time_now += 1
                            print(f'Конец видео')
                            i.time_now = 0
                    return

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
