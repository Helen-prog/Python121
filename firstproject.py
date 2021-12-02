# from tkinter import *
# import random
# root = Tk()
# root.title('Criss-cross')
# game_run = True
# field = []
# cross_count = 0
#
#
# def new_game():
#     for row in range(3):
#         for col in range(3):
#             field[row][col]['text'] = ' '
#             field[row][col]['background'] = 'lavender'
#     global game_run
#     game_run = True
#     global cross_count
#     cross_count = 0
#
#
# def click(row, col):
#     if game_run and field[row][col]['text'] == ' ':
#         field[row][col]['text'] = 'X'
#         global cross_count
#         cross_count += 1
#         check_win('X')
#         if game_run and cross_count < 5:
#             computer_move()
#             check_win('O')
#
#
# def check_win(smb):
#     for n in range(3):
#         check_line(field[n][0], field[n][1], field[n][2], smb)
#         check_line(field[0][n], field[1][n], field[2][n], smb)
#     check_line(field[0][0], field[1][1], field[2][2], smb)
#     check_line(field[2][0], field[1][1], field[0][2], smb)
#
# def check_line(a1,a2,a3,smb):
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
#         a1['background'] = a2['background'] = a3['background'] = 'pink'
#         global game_run
#         game_run = False
#
#
# def can_win(a1,a2,a3,smb):
#     res = False
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
#         a3['text'] = 'O'
#         res = True
#     if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
#         a2['text'] = 'O'
#         res = True
#     if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
#         a1['text'] = 'O'
#         res = True
#     return res
#
# def computer_move():
#     for n in range(3):
#         if can_win(field[n][0], field[n][1], field[n][2], 'O'):
#             return
#         if can_win(field[0][n], field[1][n], field[2][n], 'O'):
#             return
#     if can_win(field[0][0], field[1][1], field[2][2], 'O'):
#         return
#     if can_win(field[2][0], field[1][1], field[0][2], 'O'):
#         return
#     for n in range(3):
#         if can_win(field[n][0], field[n][1], field[n][2], 'X'):
#             return
#         if can_win(field[0][n], field[1][n], field[2][n], 'X'):
#             return
#     if can_win(field[0][0], field[1][1], field[2][2], 'X'):
#         return
#     if can_win(field[2][0], field[1][1], field[0][2], 'X'):
#         return
#     while True:
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
#         if field[row][col]['text'] == ' ':
#             field[row][col]['text'] = 'O'
#             break
#
#
# for row in range(3):
#     line = []
#     for col in range(3):
#         button = Button(root, text=' ', width=4, height=2,
#                         font=('Verdana', 20, 'bold'),
#                         background='lavender',
#                         command=lambda row=row, col=col: click(row,col))
#         button.grid(row=row, column=col, sticky='nsew')
#         line.append(button)
#     field.append(line)
# new_button = Button(root, text='new game', command=new_game)
# new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
# root.mainloop()


# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# reg = 'я'
# print(re.findall(reg, s))
# print(re.findall("12", s))
# reg = 'совпадения'
# print(re.search(reg, s))
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# reg = 'Я ищу'
# print(re.match(reg, s))
# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# s = "Ели[-ели]."
# reg = r'[А-Яа-яё.\[\]-]'
# print(re.findall(reg, s))
# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+', d))  # ['7', '+17', '-42', '0013', '0', '3']

# print(re.split(reg, s))
# print(re.sub(reg, "!", s, 1))
# ====================================

# import re

# s = "Я ищу совпадения в 2015 году. И я их на-йду в 2 счё_та."
# # reg = r'^\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# \d - [0-9]
# \w - [a-z0-9_]
# \s - [ ]
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1
# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09. 09:59v"
# reg1 = r'[0-2][0-9]:[0-5][0-9].'
# print(re.findall(reg1, s1))

# s1 = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg1 = r'\+?7\d{10}'
# print(re.findall(reg1, s1))

# s1 = "Я ищу совпадения в 2015 году. И я их на-йду в 2 счё_та."
# reg1 = r'я'


# print(re.findall(reg1, s1, re.I))

# IGNORECASE, I
# ASCII, A
# DOTALL, S
# MULTILINE, M
# VERBOSE, X
# LOCALE, L
# DEBAG

# print(re.findall(r"""
# [\w.-]+
# @  # @
# [\w.-]+
# """, 't-e.s_t@mail.ru', re.X))

# text = r"""
# Торт
# с вишней1
# вишней2
# """
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))
# # print(re.findall(r'\d+', "12 + ۳"))
# # print(re.findall(r'\d+', "12 + ۳", flags=re.ASCII))


# def validate_name(name):
#     return re.findall(r'^[\w.-]+@[\w.-]+[\w]{2,3}$', name, re.IGNORECASE)
#
#
# print(validate_name("Python_master@com.u"))
# print(validate_name("Python_master@com.uas"))

# s = "Самолет прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r'\2.\1.\3', s))
#
# s1 = "goo_gle.com and google.ru"
# reg1 = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# # reg1 = r'(\w+\.\w{2,3})'
# print(re.sub(reg1, r'http://\1', s1))

# f = open("xyz.txt", "w")
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
#
# f.close()
#
# f = open('text.txt', 'a')
# # print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-Hello-"))
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text.txt', "r") as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\n" \
#        "Строка №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
# with open("one.txt", "w") as f:
#     f.write(text)

# read_file = "one.txt"
# write_file = "two.txt"
# with open(read_file, 'r') as fr:
#     print(fr.read())

# print(os.getcwd())
# print(os.listdir(".."))
# os.mkdir("folder")
# os.makedirs("nested1/nested2/nested3")
# os.remove("two.txt")
# os.renames("test1/test1.txt", "test1/new/test2.txt")

# os.rmdir("test12")
# os.walk(top, topdown=True)

# for root, dirs, file in os.walk('test1'):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print("Директория", root, "была удалена.")


# print(os.path.split(r"D:\pythonProject1\test1\new\test2.txt")[1])
# print(os.path.dirname(r"D:\pythonProject1\test1\new\test2.txt"))
# print(os.path.basename(r"D:\pythonProject1\test1\new\test2.txt"))
# print(os.path.join("dir", "D:\pythonProject1", "files", "test.txt"))

# dirs = ["Work/F1", "Work/F2/F21"]
# for i in dirs:
#     os.makedirs(i)
#
# files = {
#     "Work": ["w.txt"],
#     "Work/F1": ["f11.txt", "f12.txt", "f13.txt"],
#     "Work/F2/F21": ["f211.txt", "f212.txt"]
# }
# for i, files in files.items():
#     for file in files:
#         file_path = os.path.join(i, file)
#         open(file_path, 'w').close()
# import time

# print(os.path.getctime(r"D:\pythonProject1\Work\F2\F21\f211.txt"))
# print(os.path.getatime(r"D:\pythonProject1\Work\F2\F21\f211.txt"))
# print(os.path.getmtime(r"D:\pythonProject1\Work\F2\F21\f211.txt"))
# print(os.path.getsize(r"D:\pythonProject1\Work\F2\F21\f211.txt"))
# atime = os.path.getatime(r"D:\pythonProject1\Work\F2\F21\f211.txt")
# mtime = os.path.getmtime(r"D:\pythonProject1\Work\F2\F21\f211.txt")
# print("Дата последнего использования файла:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print("Дата последнего редактирования файла:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# file_path = r'Work\F2\F21\f211.txt'
#
# if os.path.exists(file_path):
#     dir, name = os.path.split(file_path)
#     # print(dir)
#     # print(name)
#     atime = os.path.getatime(file_path)
#     print(name + " (" + dir + ") время последнего доступа к файлу: " + str(atime))
# else:
#     print("Файла " + file_path + " не существует")

# print(os.path.normcase('C:/User/admin/Documents'))
# print(os.path.splitdrive('/Documents/text.txt'))
# print(os.path.splitext('C:/User/admin/Documents/text.txt'))
# print(os.path.isfile(r'Work\F2\F21\f211.txt'))
# print(os.path.isdir(r'Work\F2\F21\qqqq'))

# dir_name = "Work"
#
# objs = os.listdir(dir_name)
# print(objs)
# class Point3D:
#     pass

# конструктор   __new__
# инициализатор  __init__
# деструктор  __del__


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#     count = 0
#     # WIDTH = 5
#
#     # def __new__(cls, *args, **kwargs):
#     # print("Конструктор!")
#     # return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.count += 1
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y

# def __getattr__(self, name):
#     return f"В классе {__class__.__name__} отсутствуе атрибут: {name}"
#
# def __getattribute__(self, item):
#     if item == "_Point__x":
#         return "Закрытая переменная"
#     else:
#         return object.__getattribute__(self, item)
#
# def __setattr__(self, name, value):
#     if name == "WIDTH":
#         raise AttributeError
#     else:
#         self.__dict__[name] = value


# p1 = Point(5, 20)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)
# print(p1.get_coords())
# p1.set_coords(1, 2)
# print(p1.get_coords())
# p1.set_coords_x(8)
# p1.set_coords_y(6)
# print(p1.get_coords())
# print(p1.get_coords_x())
# print(p1.get_coords_y())
# print(p1.__dict__)
# print(p1._Point__x)
# print(p1._Point__y)
# print(p1.zzz)
# print(p1.q)
# p1.WIDTH = 6


# __getattr__
# __getattribute__
# __setattr__
# __slots__

# import math
#
#
# class Rectangle:
#
#     def __init__(self, l=1, w=1):
#         print("Инициализатор")
#         self.__l = l
#         self.__w = w
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_l(self, l):
#         if Rectangle.__check_value(l):
#             self.__l = l
#
#     def set_w(self, w):
#         if Rectangle.__check_value(w):
#             self.__w = w
#
#     def get_l(self):
#         return self.__l
#
#     def get_w(self):
#         return self.__w
#
#     def s(self):
#         return self.__w * self.__l
#
#     def p(self):
#         return self.__w * 2 + self.__l * 2
#
#     def g(self):
#         return math.sqrt(self.__w * self.__w + self.__l * self.__l)
#
#     def drawing(self):
#         print(("*" * self.__w + '\n') * self.__l)
#
#
# p1 = Rectangle()
#
# p1.set_w(9)
# p1.set_l(3)
#
# print("L = ", p1.get_l())
# print("B = ", p1.get_w())
# print("S = ", p1.s())
# print("P = ", p1.p())
# print("Гипатенуза = ", round(p1.g(), 2))
# p1.drawing()

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         print("Приветствую! Меня зовут:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающий роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
#
# print("Численность роботов:", Robot.k)
# ================================================
# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Неверный формат данных")
#
#     def __get_coords_x(self):
#         return self.__x
#
#     def __del_coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = "100"  # запись значения
# x = p1.coordX  # чтение значения
# print(x)
# del p1.coordX
# p1.coordX = 7
# q = p1.coordX
# print(q)

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property
#     def coords_x(self):
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Неверный формат данных")
#
#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = "100"  # запись значения
# x = p1.coordX  # чтение значения
# print(x)
# del p1.coordX
# p1.coordX = 7
# q = p1.coordX
# print(q)


# 1 кг = 2,205 фунта

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# # weight.kg = 'десять'
# ===========================================

# Согласно модели данных Python, язык предлагает три вида
# методов: статические, класса и экземпляра класса.
# @staticmethod

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         Point.__count += 1
#         self.__x = x
#         self.__y = y
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point(3, 5)
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# print(Change.inc(2), Change.dec(3))

# cls
# @classmethod

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_str):
#         day, month, year = map(int, date_str.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '51.22.2021',
#     '30-12-2021',
#     '30.12.2021',
#     '30/12/2021'
# ]
#
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         a = date.string_to_db()
#         print(a)
#     else:
#         print("Неправильная дата или формат строки с датой")


# class Account:
#     rate_usd = 0.014
#     rate_eur = 0.012
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежит {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежит {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Процент: {self.percent: .0%}")
#         print("-" * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def add_persents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdrow_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}.")
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#             self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_persents()
# print()
# acc.withdrow_money(300)
# print()
# acc.withdrow_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdrow_money(3000)
# print()
# =================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"{self.__x}, {self.__y}"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "blue", width: int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         super().__init__(*args)
#         self.__width = 5
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольник: {self._sp}, {self._ep}, {self._color}, {self.__width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.__dict__)
# # print(line._width)
# line.draw_line()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
# # DRY (Don`t Repeat Youself) - не повторяйся!

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# rect.width = 30
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = "red"
# print(rect.color)
# print(rect.area())


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целочисленными")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10, 20), Point(100, 200))
# line.draw_line()
# rect = Rect(Point(5, 7), Point(50, 70))
# rect.set_coords(Point(5.8, 7.5), Point(50.6, 70.4))
# rect.draw_rect()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         pass
#         # raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     # def draw(self):
#     #     print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     pass
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование элипс: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-50, -50), Point(50, 50)))
#
# for f in figs:
#     f.draw()
# =================================================

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# bob = Dog("Bob")
# bob.sleep()
# bob.play()
# bob.bark()

# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#     def hi(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#     def hi(self):
#         print("B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#     def hi(self):
#         print("C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор класса D")
#
#     def call_hi(self):
#         C.hi(self)
#
#
# d = D()
# print(D.mro())
# d.call_hi()

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self):
#         print("Инициализатор Styles")
#         # super().__init__()
#
#
# class Pos:
#     def __init__(self):
#         print("Инициализатор Pos")
#         # super().__init__()
#
#
# class Line(Styles, Pos):
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# Mixin

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         super().display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#         pass
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет отображаться и регистрироваться в файле subclasslog.txt")

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целыи числом")
#
#         self.__sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if (x > 9) else "0" + str(x)
#
#     def get_second(self):
#         return self.__sec
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.__sec + other.get_second())
#
#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         self.__sec += other.get_second()
#         return self
#
#     def __eq__(self, other):
#         return self.__sec == other.get_second()
#         # if self.__sec == other.get_second():
#         #     return True
#         # return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.__sec // 3600) % 24
#         elif item == "min":
#             return (self.__sec // 60) % 60
#         elif item == "sec":
#             return self.__sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#
#         if key == "hour":
#             self.__sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.__sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.__sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# c4 = Clock(300)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 10
# c1["min"] = 20
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])
# print("Время равно", c1 == c2)
# if c1 != c4:
#     print("Время не равно")
# c1 += c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 + c2 + c4
# print(c3.get_format_time())

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пошок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, 2, 3)
# print(len(p))
# print(abs(p))
# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# print(pt.length)
# pt.length = 10
# print(pt.length)
# pt3 = Point3D(10, 20, 30)
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)

# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:!.,; ")
# print(s1(" Hello, World! "))


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c


# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# Класс как декоратор
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func1):
#         def wrap(a, b):
#             print('Перед вызовом функции')
#             print(self.name)
#             func1(a, b)
#             print('После вызовом функции')
#
#         return wrap
#
#
# @MyDecorator(6)
# def func(a, b):
#     print(a, b)
#
#
# func(2, 5)

# @MyDecorator
# def func2(a, b, c):
#     return a * b * c


# print(func2(2, 5, 2))
# ============================

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор класса ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(5))
# class Message:
#     _REGISTRY = {}
#
#     def __init__(self, text):
#         self.__text = text
#
#     def send(self):
#         raise NotImplementedError()
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTRY[name] = klass
#             return klass
#
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTRY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенжера нет.")
#         print(text, end=" ")
#
#         return klass(text)
#
#
# @Message.register('Telegram')
# class TelegramMessager(Message):
#     def send(self):
#         print("(Telegram)")
#
#
# @Message.register('WhatsApp')
# class WhatsAppMessager(Message):
#     def send(self):
#         print("(WhatsApp)")
#
#
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create("WhatsApp", "new text")
# m2.send()

#  Дескрипторы
# __get__, __set__, __delete__, __set_name__

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value

# class ValidString:
#
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# print(p.name)
# print(p.surname)
# p.name = "2"
# print(p.name)
# DRY

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)
# MyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# class MyMetaclass(type):
#     def __new__(cls, name, bases, dict):
#         print('Создание нового объекта', name)
#         return super(MyMetaclass, cls).__new__(cls, name, bases, dict)
#
#     def __init__(cls, name, bases, dict):
#         print('Инициализация класса', name)
#         super(MyMetaclass, cls).__init__(name, bases, dict)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#
# stud = Student("Анна")
# print("Имя студента:", stud.get_name())
# print("Тип объекта Student:", type(stud))
# print("Тип класса Student:", type(Student))

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(*args):
#             print(*args)
#             res = func(*args)
#             return res ** self.arg
#
#         return wrapper
#
#
# @Power(3)
# def mul(a, b):
#     return a * b
#
#
# print("Результат: ", mul(2, 2))


# списки
# словари
# кортежи
# множества

# Связанный список

# class Node:
#     def __init__(self, elem):
#         self.__data = elem
#         self.__next = None
#
#     def get_data(self):
#         return self.__data
#
#     def get_next(self):
#         return self.__next
#
#     def set_data(self, newdata):
#         self.__data = newdata
#
#     def set_next(self, newdata):
#         self.__next = newdata
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     def list_print(self):
#         val = self.head
#         while val:  # val is not None
#             print(val.get_data(), end=' ')
#             val = val.get_next()
#         print()
#
#     def add(self, item):  # добавление элементов в начало списка
#         tmp = Node(item)
#         tmp.set_next(self.head)
#         self.head = tmp
#
#     def append(self, item):  # добавление элементов в конец списка
#         tmp = Node(item)
#         if self.head is None:
#             self.head = tmp
#             return
#         end = self.head
#         while end.get_next():
#             end = end.get_next()
#         end.set_next(tmp)
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current is not None:
#             count = count + 1
#             current = current.get_next()
#         return count
#
#     def insert(self, position, item):  # вставить элемент в указанную позицию
#         if position > self.size():
#             raise IndexError("Индекс выходит за пределы списка")
#         current = self.head
#         previous = None
#         pos = 0
#         if position == 0:
#             self.add(item)
#             return
#         else:
#             new_node = Node(item)
#             while pos < position:
#                 pos += 1
#                 previous = current
#                 current = current.get_next()
#             previous.set_next(new_node)
#             new_node.set_next(current)
#
#     def search(self, item):
#         current = self.head
#         found = False
#         while current is not None and not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 current = current.get_next()
#         return found
#
#     def pop(self, position=None):  # удаление элемента в начале, если позиция не указана, если указана, удаление с
# # текущей позиции
#         ret = None
#         current = self.head
#         if position is None:
#             ret = current.get_data()
#             self.head = current.get_next()
#         elif position > self.size() - 1:
#             raise IndexError("Индекс выходит за пределы списка")
#         else:
#             pos = 0
#             previous = None
#             while pos < position:
#                 previous = current
#                 current = current.get_next()
#                 pos += 1
#                 ret = current.get_data()
#             previous.set_next(current.get_next())
#
#         print(ret)
#         return ret
#
#     def reverse(self):
#         p = self.head
#         self.head = None
#         while p is not None:
#             p0, p = p, p.get_next()
#             p0.set_next(self.head)
#             self.head = p0
#
#
# temp = LinkedList()
# temp.head = Node(93)
# temp.list_print()
#
# temp.add(31)
# temp.add(77)
# temp.append(26)
# temp.append(54)
# temp.insert(3, 17)
# temp.list_print()
# print(temp.size())
# print(temp.search(17))
#
# temp.pop()
# temp.list_print()
# temp.pop(2)
# temp.list_print()
# temp.reverse()
# temp.list_print()


# class Node:
#     def __init__(self, elem, nxt=None, prev=None):
#         self.data = elem
#         self.prev = prev
#         self.next = nxt
#
#
# class DoublyLinkedList:
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail
#
#     def is_empty(self):
#         return self.head is None and self.tail is None
#
#     def add(self, elem):
#         '''Добавляет элемент в начало списка'''
#         if self.head is None:
#             item = Node(elem)
#             self.head = item
#             self.tail = self.head
#         else:
#             item = Node(elem, self.head)
#             self.head.prev = item
#             self.head = self.head.prev
#
#     def append(self, elem):
#         '''Добавляет элемент в конец списка'''
#         if self.tail is None:
#             item = Node(elem)
#             self.head = item
#             self.tail = self.head
#         else:
#             item = Node(elem, None, self.tail)
#             self.tail.next = item
#             self.tail = item
#
#     def pop(self):
#         '''удаление из конца списка'''
#         if self.head == self.tail:
#             self.head = self.tail = None
#             return
#         self.tail = self.tail.prev
#         self.tail.next = None
#
#     def shift(self):
#         '''убирает элемент из начала списка'''
#         if self.head == self.tail:
#             self.head = self.tail = None
#             return
#         self.head = self.head.next
#         self.head.prev = None
#
#     def print(self):
#         val = self.head
#         print("Список ссылок:")
#         while val:
#             print(val.data)
#             val = val.next
#         print()
#
#
# links = [
#     'http://site.ru',
#     'http://site.ru/news',
#     'http://site.ru/contacts',
#     'http://site.ru/about',
# ]
# link = DoublyLinkedList()
# for name in links:
#     link.add(name)
#
# while True:
#     if not link.is_empty():
#         link.print()
#     else:
#         print("Список ссылок пуст!\n")
#     print('1 - добивить элемент в начало списка')
#     print('2 - добивить элемент в конец списка')
#     print('3 - удалить элемент из конца списка')
#     print('4 - удалить элемент из начала списка')
#     print('5 - выйти')
#     operation = input('-> ')
#     if operation == "1":
#         a = input("Новая ссылка: ")
#         link.add(a)
#     elif operation == "2":
#         a = input("Новая ссылка: ")
#         link.append(a)
#     elif operation == "3":
#         link.pop()
#     elif operation == "4":
#         link.shift()
#     elif operation == "5":
#         print("Всего доброго!")
#         break

# LIFO Стек

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return f"{self.stack}"
#
#     def is_empty(self):
#         return self.stack == []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         return self.stack.pop()
#
#     def size(self):
#         return len(self.stack)
#
#     def show(self):
#         return self.stack


# brackets = {
#     ')': '(',
#     '>': '<'
# }
#
#
# def balanced_brackets(text):
#     s = Stack()
#     for c in text:
#         if c in brackets.values():
#             s.push(c)
#         elif c in brackets:
#             if s.is_empty():
#                 return False
#             elif brackets[c] != s.pop():
#                 return False
#
#     return s.is_empty()
#
#
# print(balanced_brackets('(<x)>(())()'))
# print(balanced_brackets('<((<<hello>>))>'))


# Очередь (FIFO - first in first out - первым пришел, первым ушел)

# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def push(self, item):
#         self.queue.append(item)
#
#     def pop(self):
#         if len(self.queue) == 0:
#             return None
#         return self.queue.pop(0)
#
#     def show(self):
#         return self.queue
#
#
# s = Queue()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.show())
# s.pop()
# s.pop()
# print(s.show())

# Бинарное дерево поиска (BST - binary search tree)
#  left < node < right

# class Node:
#
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
#     def findval(self, val):
#         if val < self.data:
#             if self.left is None:
#                 return str(val) + " - not found"
#             return self.left.findval(val)
#         elif val > self.data:
#             if self.right is None:
#                 return str(val) + " - not found"
#             return self.right.findval(val)
#         else:
#             return str(self.data) + " - is found"
#
#
#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.data, end=" ")
#         if self.right:
#             self.right.print_tree()
#
#
# root = Node(10)
# root.insert(6)
# root.insert(14)
# root.insert(12)
# root.insert(3)
# root.print_tree()
# print()
# print(root.findval(7))
# print(root.findval(14))

# =============================
# Сериализация - процесс перевода какой-либо структуры данных в последовательность битов
# Десериализация - восставновление начального состояния структуры данных из битовой последовательности
# marshal (.pyc)
# pickle
# json

# dump()
# dumps()
# load()
# loads()

import pickle

# filename = "basket.txt"
# shoplist = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# # запись в файл
# with open(filename, "wb") as fh:
#     pickle.dump(shoplist, fh)
#
# # считывание из файла
# with open(filename, "rb") as fh:
#     a = pickle.load(fh)
# print(a)

# class Test:
#     a_number = 35
#     a_string = "привет"
#     a_list = [1, 2, 3]
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#     a_tuple = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Test.a_number}\nСтрока: {Test.a_string}\nСписок: {Test.a_list}\nСловарь: " \
#                f"{Test.a_dict}\nКортеж: {Test.a_tuple}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# print(pickle.loads(my_obj))

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename)
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename)
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# print(reader.read_line())
# print(reader.read_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())

# import json
#
# date = {
#     'firstname': "Ирина",
#     "lastname": "Доу",
#     "age": 35,
#     "children": [
#         {
#             "firstname": "Алиса",
#             "age": 6
#         },
#         {
#             "firstname": "Боб",
#             "age": 8
#         }
#     ]
# }
# json_string = json.dumps(date, sort_keys=True, ensure_ascii=False)
# print(json_string)
#
# data = json.loads(json_string)
# print(data)
# with open("data_file.json", "w") as fw:
#     json.dump(date, fw, indent=2)
#
# with open("data_file.json", "r") as fw:
#     data = json.load(fw)
#     print(data)


# requests

import random as r
import time as t


#
#
# def bubble(array):
#     for i in range(len(a) - 1):
#         for j in range(len(a) - i - 1):
#             if array[j] > array[j + 1]:
#                 buff = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = buff
#             # print(*a)
#             # print('---------------')
#
#
# a = [r.randint(1, 99) for i in range(1000)]
#
# print(a)
# start = t.monotonic()
# bubble(a)
# print(a)
# res = t.monotonic() - start
# print(round(res, 3), "sec")  # 0.031 sec

# функция слияния двух отсортированных списков
# def merge_sort(x, y):
#     z = []
#     n = len(x)
#     m = len(y)
#
#     i = 0
#     j = 0
#     while i < n and j < m:
#         if x[i] <= y[j]:
#             z.append(x[i])
#             i += 1
#         else:
#             z.append(y[j])
#             j += 1
#
#     z += x[i:] + y[j:]
#     return z
#
#
# # функция деления списка и слияния списков в общий отсортированный список
# def split_merge(x):
#     n1 = len(x) // 2
#     a1 = x[:n1]  # деление массива на два примерно равной длины
#     a2 = x[n1:]
#
#     if len(a1) > 1:  # если длина 1-го списка больше 1, то делим дальше
#         a1 = split_merge(a1)
#     if len(a2) > 1:  # если длина 2-го списка больше 1, то делим дальше
#         a2 = split_merge(a2)
#
#     return merge_sort(a1, a2)  # слияние двух отсортированных списков в один
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# split_merge(a)
# print(a)


# def sum_list(lst):
#     if len(lst) == 1:  # строка 2
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:]) # строка 5
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# ==================================
# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         print("===============================================")
#         print(n)
#         print("===============================================")
#         return convert[n]
#     else:
#         print(n)
#         a = to_str(n // base, base)
#         print(n)
#         # print(a)
#         b = a + convert[n % base]
#         # print("b", b)
#         return b
# return convert[n] if n < base else to_str(n // base, base) + convert[n % base]


# print(to_str(255, 10))  # FF
# to_str(2551230780, 10)

# def elevator(n):  # n - номер этажа
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# import random as r
#
#
# def bubble(array):
#     for i in range(len(a) - 1):
#         for j in range(len(a) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#             print(a)
#             print('-' * 20)
#
#
# a = [r.randint(1, 99) for i in range(10)]
#
# print(a)
# bubble(a)
# print(a)

# Реализация пирамидальной сортировки на Python

# def heap_sort (sequence):
#
#     def swap_items (index1, index2):
#         if sequence[index1] < sequence[index2]:                                 # !
#             sequence[index1], sequence[index2] = sequence[index2], sequence[index1]
#
#     def sift_down (parent, limit):
#         while True:
#             child = parent * 2 + 2  # То же, что и parent * 2 + 2
#             if child < limit:
#                 if (sequence[child] < sequence[child - 1]):
#                     swap_items(parent, child-1)
#                     parent = child-1
#                 else:
#                     swap_items(parent, child)
#                     parent = child
#             else:
#                 if (child-1<limit):
#                     swap_items(parent,child-1)
#                 break
#     # Тело функции heap_sort
#     length = len(sequence)
#     # Формирование первичной пирамиды
#     for index in range((length >> 1) - 1, -1, -1):
#         sift_down(index, length)
#     # Окончательное упорядочение
#     for index in range(length - 1, 0, -1):
#         swap_items(index, 0)
#         sift_down(0, index)
#
#
# lst = [2, 11, 3, 14, 1, 5, 8, 15, 9, 7, 10, 4, 13, 6, 12]
# heap_sort(lst)
# print(lst)

# from heapq import heappop, heappush
#
#
# def heap_sort(array):
#     heap = []
#
#     for element in array:
#         heappush(heap, element)
#
#     ordered = []
#
#     # While we have elements left in the heap
#     while heap:
#         ordered.append(heappop(heap))
#
#     return ordered
#
#
# array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
# print(heap_sort(array))


# def heapify(arr, n, i):
#     # Find largest among root and children
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#
#     if l < n and arr[i] < arr[l]:
#         largest = l
#
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#
#     # If root is not largest, swap with largest and continue heapifying
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
#
# def heap_sort(arr):
#     n = len(arr)
#
#     # Build max heap
#     for i in range(n, 0, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
#
# lst = [12, 11, 13, 5, 6, 7]
# heap_sort(lst)
# print(lst, end=" ")


# from math import floor


# def big_endian(arr, start, end):
#     root = start
#     while True:
#         child = root * 2 + 1
#         if child >= end:
#             break
#         if child + 1 < end and arr[child] < arr[child + 1]:
#             child = child + 1
#         if arr[root] < arr[child]:
#             arr[root], arr[child] = arr[child], arr[root]
#             root = child
#         else:
#             break
#
#
# def heap_sort(arr):
#     n = len(arr)
#     for begin in range((n - 1) // 2, -1, -1):
#         big_endian(arr, begin, n)
#     for end in range(n - 1, 0, -1):
#         arr[0], arr[end] = arr[end], arr[0]
#         big_endian(arr, 0, end)
#     return arr
#
#
# lst = [2, 11, 3, 14, 1, 5, 8, 15, 9, 7, 10, 4, 13, 6, 12]
# heap_sort(lst)
# print(lst, end=" ")


# def MAX_Heapify(heap, HeapSize, root):  # Внести структурные изменения в кучу, чтобы значение родительского узла было больше, чем дочернего узла.
#
#     left = 2 * root + 1
#     right = left + 1
#     larger = root
#     if left < HeapSize and heap[larger] < heap[left]:
#         larger = left
#     if right < HeapSize and heap[larger] < heap[right]:
#         larger = right
#         # if larger == root:  # Если скорректирована куча, значение больше равно левому или правому узлу, в это время
#     # выполните операцию подкачки
#     if heap > root:
#         heap[larger], heap[root] = heap[root], heap[larger]
#         MAX_Heapify(heap, HeapSize, larger)
#
#
# def Build_MAX_Heap(heap):  # Построить кучу и изменить порядок всех данных в куче
#     HeapSize = len(heap)  # Удобно брать только длину кучи для i в диапазоне
#     for i in ((HeapSize - 2) // 2, -1, -1):  # отсчет от начала до конца
#         MAX_Heapify(heap, HeapSize, i)
#
#
# def heap_sort(heap):  # Извлеките корневой узел и настройте его с последним, и продолжите процесс настройки для предыдущих узлов len-1.
#     Build_MAX_Heap(heap)
#     for i in range(len(heap) - 1, -1, -1):
#         heap[0], heap[i] = heap[i], heap[0]
#         MAX_Heapify(heap, i, 0)
#     return heap
#
#
# array = [2, 11, 3, 14, 1, 5, 8, 15, 9, 7, 10, 4, 13, 6, 12]
# # array = []
# # for i in range(2,5000):
# #    #print(i)
# #    array.append(random.randrange(1,i))
#
# print(array)
# # start_t = time.time()
# heap_sort(array)
# # end_t = time.time()
# # print("cost:", end_t - start_t)
# print(array)
# print(l)
# heap_sort(l)
# print(l)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Порождающие паттерны
# Фабричный метод, Factory Method, Виртуальный конструктор

# Есть компания, которая занимается грузоперевозками. Для автоматизации процессов нужна программа для организации этих
# перевозок. Вы ее реализовали. Но у вас появился запрос на организацию не только сухопутных перевозок, но еще и морских
# А потом может и авиаперевозок

# from abc import ABC, abstractmethod
#
#
# class Logistics(ABC):
#
#     @abstractmethod
#     def create_transport(self):
#         pass
#
#     def connect_to_db(self):
#         pass
#
#     def get_data_from_db(self):
#         pass
#
#
# class GroundLogistics(Logistics):
#     def create_transport(self):
#         return Truck()
#
#
# class SeaLogistics(Logistics):
#     def create_transport(self):
#         return Boat()
#
#
# class ITransport:
#     def diliver(self):
#         pass
#
#
# class Truck(ITransport):
#     def deliver(self):
#         print('Грузовик едит по суше')
#
#
# class Boat(ITransport):
#     def deliver(self):
#         print('Лодка плывет по воде')
#
#
# ground_logistic = GroundLogistics()
# sea_logistic = SeaLogistics()
#
# truck = ground_logistic.create_transport()
# truck.deliver()
#
# boat = sea_logistic.create_transport()
# boat.deliver()


# ++++++++++++++++++++++++++++++++++++
# def shell_sort(s):
#     count = len(s) // 2
#     while count > 0:
#
#         for start in range(count):
#             gap_insertion_sort(s, start, count)
#
#         print("После увеличения размера", count, "Список:", s)
#
#         count = count // 2
#
#
# def gap_insertion_sort(s, start, gap):
#     for i in range(start + gap, len(s), gap):
#         current = s[i]
#         pos = i
#
#         while pos >= gap and s[pos - gap] > current:
#             s[pos] = s[pos - gap]
#             pos = pos - gap
#
#         s[pos] = current
# def shell_sort(data):
#     inc = len(data) // 2
#     while inc:
#         for i, el in enumerate(data):
#             while i >= inc and data[i - inc] > el:
#                 data[i] = data[i - inc]
#                 i -= inc
#             data[i] = el
#         inc = 1 if inc == 2 else int(inc * 5.0 / 11)
#     return data

# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         # print("После увеличения размера", gap, "Список:", s)
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)

# class MusicPlayer:
#     def play_music(self):
#         print("Проигрываю музыку")
#
#     def open_photo(self):
#         print("Открываю фотографию")
#
#
# m1 = MusicPlayer()
# m1.play_music()
# m1.open_photo()


# class Book:
#     def __init__(self, name, author_name, year, price):
#         self.name = name
#         self.author_name = author_name
#         self.year = year
#         self.price = price
#
#     # def __str__(self):
#     #     return f"{self.name} {self.author_name} {self.year} {self.price}"
#
#
# class Invoice:  # Счет
#     def __init__(self, book, quantity, discount_rate, tax_rate, pr):
#         self.book = book
#         self.quantity = quantity  # количество
#         self.discount_rate = discount_rate  # Размер скидки
#         self.tax_rate = tax_rate  # Ставка налога
#         self.total = self.calculate_total(pr)
#
#     # def __str__(self):
#     #     return f"{self.book} {self.quantity} {self.discount_rate} {self.tax_rate}"
#
#     def calculate_total(self, pr):
#         price = (pr.price - (pr.price * self.discount_rate) / 100) * self.quantity
#         price_width_taxes = price - price * self.tax_rate / 100
#         return price_width_taxes
#
#     def print_invoice(self, pr):
#         print(self.quantity, " книги '", self.book, "' ", pr.price, " руб", sep="")
#         print("Размер скидки: ", self.discount_rate, "%", sep="")
#         print("Ставка налога: ", self.tax_rate, "%", sep="")
#         print("Всего: ", self.calculate_total(pr), "руб")
#
#     def save_to_file(self):
#         pass
#
#
# b1 = Book("Изучаем программирование на Python", "Пол Бэрри", 2021, 2000)
# inv = Invoice("Изучаем программирование на Python", 3, 5, 2, b1)
# inv.print_invoice(b1)
# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
# f = open('text2.txt', 'r')
# s = f.readlines()
# print(s)
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos < len(s):
#     del s[pos]
# else:
#     print("Индекс введен неверно!")
# print(s)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(s)
# f.close()

print("Вносим изменения")
