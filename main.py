# Завдання 1
# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
            print('Рядок додано до стеку.')
        else:
            print('Рядок не додано, тому що стек повний.')

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print('Стек порожній.')

    def count(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack = []
        print('Стек очищено.')

    def get_value(self):
        if not self.empty():
            return self.stack[-1]
        else:
            print('Стек порожній')

    def display(self):
        print('Меню:')
        print("1. Додати рядок до стеку")
        print("2. Виштовхнути рядок зі стеку")
        print("3. Кількість рядків у стеку")
        print("4. Перевірити, чи порожній стек")
        print("5. Перевірити, чи повний стек")
        print("6. Очистити стек")
        print("7. Отримати значення без виштовхування верхнього рядка зі стеку")
        print("0. Вийти з програми")

        while True:
            choice = input('Введіть ваш вибір:')

            if choice == '1':
                item = input('Введіть рядок для додавання до стеку:')
                self.push(item)
            elif choice == '2':
                deleted_row = self.pop()
                if deleted_row is not None:
                    print('Виштовхнутий рядок:', deleted_row)
            elif choice == '3':
                print('Кількість рядків у стеку:', self.count())
            elif choice == '4':
                if self.empty():
                    print('Стек порожній.')
                else:
                    print('Стек не порожній.')
            elif choice == '5':
                if self.full():
                    print('Стек повний.')
                else:
                    print('Стек не повний.')
            elif choice == '6':
                self.clear()
            elif choice == '7':
                top_item = self.get_value()
                if top_item is not None:
                    print('Значення першого рядка без виштовхування:', top_item)
            elif choice == '0':
                print('Програма завершена.')
                break
            else:
                print('Некоректний вибір.')

size = int(input('Введіть максимальний розмір стеку: '))
stack = Stack(size)
stack.display()


# Завдання 2
# Змініть стек із першого завдання таким чином, щоб його
# розмір був нефіксованим.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print('Рядок додано до стеку.')

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print('Стек порожній.')

    def count(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def full(self):
        return False

    def clear(self):
        self.stack = []
        print('Стек очищено.')

    def get_value(self):
        if not self.empty():
            return self.stack[-1]
        else:
            print('Стек порожній')

    def display(self):
        print('Меню:')
        print("1. Додати рядок до стеку")
        print("2. Виштовхнути рядок зі стеку")
        print("3. Кількість рядків у стеку")
        print("4. Перевірити, чи порожній стек")
        print("5. Перевірити, чи повний стек")
        print("6. Очистити стек")
        print("7. Отримати значення без виштовхування верхнього рядка зі стеку")
        print("0. Вийти з програми")

        while True:
            choice = input('Введіть ваш вибір:')

            if choice == '1':
                item = input('Введіть рядок для додавання до стеку:')
                self.push(item)
            elif choice == '2':
                deleted_row = self.pop()
                if deleted_row is not None:
                    print('Виштовхнутий рядок:', deleted_row)
            elif choice == '3':
                print('Кількість рядків у стеку:', self.count())
            elif choice == '4':
                if self.empty():
                    print('Стек порожній.')
                else:
                    print('Стек не порожній.')
            elif choice == '5':
                if self.full():
                    print('Стек повний.')
                else:
                    print('Стек не повний.')
            elif choice == '6':
                self.clear()
            elif choice == '7':
                top_item = self.get_value()
                if top_item is not None:
                    print('Значення першого рядка без виштовхування:', top_item)
            elif choice == '0':
                print('Програма завершена.')
                break
            else:
                print('Некоректний вибір.')

stack = Stack()
stack.display()

# Завдання 3
# Дано три вежі та n дисків різного розміру, відсортованих
# за зростанням, розміщених на першій вежі у вигляді піраміди.
# Потрібно перемістити всі диски на третю вежу,
# використовуючи проміжну вежу, за умови, що можна
# переміщати тільки один диск за раз та диск завжди можна
# покласти лише на диск більшого розміру або на порожню
# вежу.
# Ця задача може бути вирішена за допомогою
# рекурсивного алгоритму, використовуючи стек для
# зберігання проміжних ходів при переміщенні дисків між
# вежами.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def move_disk(start, end):
    print(f'Перемістити диск із стержня {start} на стержень {end}')

def hanoi(n, start, end, aux, stack):
    if n == 1:
        move_disk(start, end)
    else:
        hanoi(n-1, start, aux, end, stack)
        move_disk(start, end)
        hanoi(n - 1, aux, end, start, stack)

def hanoi_solve(n):
    stack = Stack()
    hanoi(n, 'A', 'C', 'B', stack)

n = int(input('Введіть кількість дисків:'))

hanoi_solve(n)
