def first():
    """
    Будет выведена строка 'spam', функция обращается к глобальной переменной в объемлющем модуле.
    """

    print('--1--')
    x = 'spam'

    def func():
        print(x)
    func()


def second():
    """
    Будет выведена строка 'spam'
    """

    print('--2--')
    x = 'spam'

    def func():
        x = 'ni!'

    func()
    print(x)


def third():
    """
    Первой строкой 'ni!' - x в локальной облати
    Второй строкой 'spam' - x в глобальная области
    """

    print('--3--')
    x = 'spam'

    def func():
        x = 'ni!'
        print(x)

    func()
    print(x)


def fourth():
    """
    Будет выведена строка 'spam', т.к. x объявлена как глобальная
    """

    print('--4--')
    global x
    x = 'spam'

    def func():
        global x
        x = 'ni!'

    func()
    print(x)


def fifth():
    """
    Первой строкой 'ni!' - значение x из объемлющей функции
    Второй строкой 'spam' - в глобальной области
    """

    print('--5--')
    x = 'spam'

    def func():
        x = 'ni!'

        def nested():
            print(x)

        nested()
    func()
    print(x)


def sixth():
    print('--6--')

    def func():
        x = 'ni!'

        def nested():
            nonlocal x
            x = 'spam'

        nested()
        print(x)
    func()

if __name__ == '__main__':
    help(first)
    first()
    help(second)
    second()
    help(third)
    third()
    help(fourth)
    fourth()
    help(fifth)
    fifth()
    help(sixth)
    sixth()