def first():
    print('--1--')
    x = 'spam'

    def func():
        print(x)
    func()


def second():
    print('--2--')
    x = 'spam'

    def func():
        x = 'ni!'

    func()
    print(x)


def third():
    print('--3--')
    x = 'spam'

    def func():
        x = 'ni!'
        print(x)

    func()
    print(x)


def fourth():
    print('--4--')
    global x
    x = 'spam'

    def func():
        global x
        x = 'ni!'

    func()
    print(x)


def fifth():
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
    first()
    second()
    third()
    fourth()
    fifth()
    sixth()