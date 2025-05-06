from pycparser.ply.yacc import resultlimit
from selenium.webdriver.common.devtools.v113.debugger import resume

class MemoryCalcZeroDivisionError(ZeroDivisionError):
    """Собственное исключение для деления на ноль в MemoryCalc."""
    def __init__(self, message="Attempt to divide by zero in MemoryCalc"):
        super().__init__(message)

class MemoryStackEmptyError(IndexError):
    """Собственное исключение, когда память пуста."""
    def __init__(self, message="Memory stack is empty"):
        super().__init__(message)

class MemoryValueError(ValueError):
    """Собственное исключение для невалидного значения в память."""
    def __init__(self, message="Only numeric values can be stored in memory"):
        super().__init__(message)

class BasicCalc:
    @staticmethod
    def _sanitize(value):
        """Проверяет, что значение числовое. Если нет — возвращает 0."""
        return value if isinstance(value, (int, float)) else 0

    @classmethod
    def _validate_operands(cls, a, b):
        """Проверяет и приводит аргументы к числам или 0."""
        return cls._sanitize(a), cls._sanitize(b)

    @classmethod
    def add(cls, a, b=None):
        if b is None:
            if isinstance(a, (list, tuple, set)):
                a = [cls._sanitize(i) for i in a]
                return sum(a)
            return cls._sanitize(a)
        a, b = cls._validate_operands(a,b)
        return a + b

    @classmethod
    def subtract(cls, a, b):
        a, b = cls._validate_operands(a, b)
        return a - b

    @classmethod
    def multiply(cls, a, b):
        a, b = cls._validate_operands(a, b)
        return a * b

    @classmethod
    def divide(cls, a, b):
        a, b = cls._validate_operands(a, b)
        if b == 0:
            raise MemoryCalcZeroDivisionError()
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
        if not isinstance(value, (int, float)):
            raise MemoryValueError()
        if len(self.memory_stack) < 3:
            self.memory_stack.append(value)
        else:
            self.memory_stack.pop(0)
            self.memory_stack.append(value)

    def memo_minus(self):
        """Извлекает (и удаляет) последнее значение из памяти."""
        if self.memory_stack:
            return self.memory_stack.pop()
        raise MemoryStackEmptyError()

    @property
    def memory_top(self):
        """Read-only свойство — вершина памяти."""
        return self.memory_stack[-1] if self.memory_stack else 0

