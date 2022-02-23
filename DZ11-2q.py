class MyOwnErr(BaseException):
    def __init__(self, txt):
        self.txt = txt


in_data = input("Разделим 100 на Ваше число введите число: ")
try:
    if in_data == 0:
        raise MyOwnErr("Деление на ноль невозможно!")
except MyOwnErr as err:
    print(err)
else:
    print(100 / float(in_data.replace(',', '.')))
finally:
    print("The end")
