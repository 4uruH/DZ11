class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    storage = {}
    serial_nums_cache = {}

    @classmethod
    def receive(cls, param):
        sku, serial, name = param
        try:
            sku = cls.validator(sku, name)
        except MyError as err:
            return print(err)
        check = serial.split()
        for i in cls.serial_nums_cache.values():
            if check == i:
                return print(f'!!!{name} с серийным номером {serial} уже находится на складе!!!')
        if name in cls.serial_nums_cache:
            cls.serial_nums_cache[name].append(serial)
        else:
            serial = serial.split()
            cls.serial_nums_cache[name] = serial
        if sku in cls.storage:
            print(f'{name} успешно принят на склад.')
            cls.storage[sku] += 1
        else:
            print(f'{name} успешно принят на склад.')
            cls.storage[sku] = 1

    @staticmethod
    def validator(param, param2):
        if param2 == 'Printer' or param2 == 'Xerox':
            if type(param[3]) is not int:
                raise MyError(
                    f'Параметр скорости печати задан неправильно. Это означает, что такого {param2} не существует.')
            else:
                return param
        else:
            return param


class Devices:
    brand = ''
    manufacturer = ''


class Printer(Devices):

    def __init__(self, brand, manufacturer, format_of_printing, speed_of_printing, serial_num):
        Devices.brand = brand
        Devices.manufacturer = manufacturer
        self.serial_num = serial_num
        self.format_of_printing = format_of_printing
        self.speed_of_printing = speed_of_printing
        self.sku = (brand, manufacturer, format_of_printing, speed_of_printing)

    def __call__(self):
        return self.sku, self.serial_num, self.__class__.__name__


class Scanner(Devices):

    def __init__(self, brand, manufacturer, scanner_type, transfer_of_scans, serial_num):
        Devices.brand = brand
        Devices.manufacturer = manufacturer
        self.serial_num = serial_num
        self.scanner_type = scanner_type
        self.transfer_of_scans = transfer_of_scans
        self.sku = (brand, manufacturer, scanner_type, transfer_of_scans)

    def __call__(self):
        return self.sku, self.serial_num, self.__class__.__name__


class Xerox(Devices):

    def __init__(self, brand, manufacturer, format_of_printing, speed_of_printing, serial_num):
        Devices.brand = brand
        Devices.manufacturer = manufacturer
        self.serial_num = serial_num
        self.format_of_printing = format_of_printing
        self.speed_of_printing = speed_of_printing
        self.sku = (brand, manufacturer, format_of_printing, speed_of_printing)

    def __call__(self):
        return self.sku, self.serial_num, self.__class__.__name__


my_printer_1 = Printer('PIXMA', 'Canon', 'Laser', '20', '1P353400002320RU')
my_printer_2 = Printer('HL-1110R', 'Brother', 'Flow', 10, '1P993400002320RU')
my_printer_3 = Printer('PIXMA', 'Canon', 'Laser', 20, '1P863400002320US')
my_xerox_1 = Xerox('HP', '107a', 'Laser', 40, '1X353400002320AT')

Warehouse.receive(my_printer_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.receive(my_xerox_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.receive(my_xerox_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.receive(my_printer_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.receive(my_printer_3())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.dispatch(my_printer_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.dispatch(my_printer_2())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.dispatch(my_xerox_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)
Warehouse.receive(my_xerox_1())
print(Warehouse.storage)
print(Warehouse.serial_nums_cache)
print('-' * 100)