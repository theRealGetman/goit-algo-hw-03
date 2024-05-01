class Stack:
    def __init__(self, name=''):
        self.stack = []
        self.name = name

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.stack)
    
    def __str__(self) -> str:
        return str(self.stack)
    
    def __repr__(self) -> str:
        return str(self.stack)
    

def hanoi(n, sticks, source: Stack, target: Stack, auxiliary: Stack):
    if n > 0:
        # Переміщаємо (n-1) дисків з початкового стрижня на допоміжний стрижень
        hanoi(n - 1, sticks, source, auxiliary, target)
        # Переміщаємо найбільший диск з початкового стрижня на кінцевий стрижень
        print(f"Перемістити диск з {source.name} на {target.name}: {n}")
        value = source.pop()
        target.push(value)
        print(f'Проміжний стан: {sticks}')
        # Переміщаємо (n-1) дисків з допоміжного стрижня на кінцевий стрижень
        hanoi(n - 1, sticks, auxiliary, target, source)
    

def play(disks_amount: int):
    sticks = {
              'A': Stack(name='A'),
              'B': Stack(name='B'), 
              'C': Stack(name='C'),
             }
    
    for n in range(disks_amount, 0, -1):
        sticks['A'].push(n)
    
    print(f'Початковий стан: {sticks}')
    hanoi(disks_amount, sticks, sticks['A'], sticks['C'], sticks['B'])
    print(f'Кінцевий стан: {sticks}')


disks_amount = int(input('Скільки дисків ти хочеш використати? '))
play(disks_amount)
