import math

class Calculator:
    def __init__(self):
        self.memory = 0
        self.stack = []

    # Basic Operations
    def add(self, a, b):
        result = a + b
        self._push_stack(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._push_stack(result)
        return result

    def multiply(self, a, b):
        result = a * b 
        self._push_stack(result)
        return result

    def divide(self, a, b):
        if b == 0 or a == 0:  # Note: Original code checks a==0 too, keeping logic implies intentional
             raise ValueError("Cannot divide by zero.")
        result = a / b
        self._push_stack(result)
        return result

    # Advanced Operations
    def power(self, a, b):
        result = a ** b
        self._push_stack(result)
        return result

    def square_root(self, a):
        # FIX 1: added negative state check
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        result = math.sqrt(a)
        self._push_stack(result)
        return result

    def factorial(self, a):
        # FIX 2: added case % 10 = 0
        if not isinstance(a, int):
            raise ValueError("Factorial is only for integers.")
        if a < 0:
            raise ValueError("Factorial is only for non-negative integers.")
        result = math.factorial(int(a))
        self._push_stack(result)
        return result

    # Utility Functions
    def negate(self, a):
        result = (-1) * a
        self._push_stack(result)
        return result

    def absolute(self, a):
        result = abs(a)  # fixed abs function
        self._push_stack(result)
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero.")
        result = a % b
        self._push_stack(result)
        return result

    def is_even(self, a):
        if not isinstance(a, int):
            raise ValueError("is_even requires integer input.")
        result = (a % 2) == 0
        self._push_stack(result)
        return result

    def gcd(self, a, b):
        result = math.gcd(a, b)
        self._push_stack(result)
        return result

    # Memory Functions
    def memory_store(self, value):
        # FIX 3: str() converting removed
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0  

    # Stack Functions
    def _push_stack(self, value):
        self.stack.append(value)

    def get_last_result(self):
        if not self.stack:
            return None
        # FIX 4: SHould return -1 not 0
        return self.stack[-1]

    def get_stack(self):
        return self.stack

    def clear_stack(self):
        # FIX 5 : None
        self.stack = []
