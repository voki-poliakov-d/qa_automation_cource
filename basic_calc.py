from pycparser.ply.yacc import resultlimit
from selenium.webdriver.common.devtools.v113.debugger import resume


class BasicCalc:
    @staticmethod
    def add (a, b= None):
        if b is None:
            if isinstance(a, (list, tuple, set)):
                return sum(a)
            return a
        return a + b

    @staticmethod
    def subtract (a, b):
        return a - b

    @staticmethod
    def multiply (a, b):
        return a * b

    @staticmethod
    def divide (a, b):
        return a / b

class MemoryCalc(BasicCalc):
    def __init__(self):
        self.memory_stack = []

    def add(self, a, b=None):
        if b is None:
            b = self._get_memory()
        result = super().add(a, b)
        self.memo_plus(result)
        return  result

    def subtract(self, a, b=None):
        if b is None:
            b = self._get_memory()
        result = super().subtract(a, b)
        self.memo_plus(result)
        return result

    def multiply(self, a, b=None):
        if b is None:
            b = self._get_memory()
        result = super().multiply(a, b)
        self.memo_plus(result)
        return result

    def divide(self, a, b=None):
        if b is None:
            b =self._get_memory()
        result = super().divide(a, b)
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
        """Извлекает последнее значение из памяти."""
        if self.memory_stack:
            return self.memory_stack.pop()
        else:
            return "Error, stack is empty"

    def _get_memory(self):
        return self.memory_stack[-1] if self.memory_stack else 0

    @property
    def memory_top(self):
        """Read-only свойство — вершина памяти."""
        return self._get_memory()
