class Date:
    def __init__(self, date_input):
        self.date_input = date_input

    @classmethod
    def date_parse(cls, self):
        d, m, y = self.date_input.split('-')
        return int(d), int(m), int(y)

    @staticmethod
    def date_val(par):
        d, m, y = par
        if d <= 0 or d > 31:
            return ValueError('дата должна быть в диапазоне от 0 до 31')
        elif m <= 0 or m > 12:
            return ValueError('параметр месяца должен быть от 0 до 12')
        elif len(str(y)) != 4:
            return ValueError('в параметре год должно быть 4 цифры')
        else:
            return 'Данные введены верно'


a = Date('21-12-222')
print(a.date_parse(a))
print(a.date_val(a.date_parse(a)))
