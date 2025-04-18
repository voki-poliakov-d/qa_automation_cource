from pycparser.ply.yacc import resultlimit
from selenium.webdriver.common.devtools.v113.debugger import resume


class BasicCalc:
    @staticmethod
    def add(a, b=None):
        if b is None:
            if isinstance(a, (list, tuple, set)):
                return sum(a)
            return a
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


class MemoryCalc(BasicCalc):
    def __init__(self):
        self.memory_stack = []

    def add(self, a, b=None):
        return self._calc_with_memory(super().add, a, b)

    def subtract(self, a, b=None):
        return self._calc_with_memory(super().subtract, a, b)

    def multiply(self, a, b=None):
        return self._calc_with_memory(super().multiply, a, b)

    def divide(self, a, b=None):
        return self._calc_with_memory(super().divide, a, b)

    def _calc_with_memory(self, operation, a, b):
        """Выполняет операцию, используя значение из памяти, если b не передано."""
        if b is None:
            b = self.memo_minus()
        result = operation(a, b)
        self.memo_plus(result)
        return result

    def memo_plus(self, value):
        """Добавляет значение в память (до 3 элементов)."""
        if len(self.memory_stack) < 3:
            self.memory_stack.append(value)
        else:
            self.memory_stack.pop(0)
            self.memory_stack.append(value)

    def memo_minus(self):
        """Извлекает (и удаляет) последнее значение из памяти."""
        if self.memory_stack:
            return self.memory_stack.pop()

    raise IndexError("Memory stack is empty")

    def _get_memory(self):
        """Просто читает значение из вершины памяти, не удаляя."""
        if self.memory_stack:
            return self.memory_stack[-1]
        return 0

    @property
    def memory_top(self):
        """Read-only свойство — вершина памяти."""
        return self._get_memory()
