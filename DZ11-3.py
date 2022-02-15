class ChekNumber:
    def __init__(self, inpt):
        self.inpt = inpt.replace(',', '.')

    @property
    def is_number(self):
        try:
            float(self.inpt)
            return True
        except ValueError:
            return False


result_list = []
while True:
    user_answer = input('Введите число для добавления в список! или stop для остановки программы : ')
    if user_answer == 'stop':
        print(f'программа остановлена, финальный список {result_list}')
        break
    if ChekNumber(user_answer).is_number is True:
        print(f'в финальный список добавлено число {user_answer}')
        result_list.append(float(user_answer.replace(',', '.')))
    else:
        print('Вы ввели НЕ число, попробуйте заново')
