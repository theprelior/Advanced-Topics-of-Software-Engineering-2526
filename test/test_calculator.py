import pytest
from calculator import Calculator


class TestCalculator:
    # --- Basic Operations ---
    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 2) == 3
        assert calc.get_stack() == [3]

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(4, 2) == 2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 5) == 10

    def test_divide(self):
        calc = Calculator()
        assert calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
        # Also test the specific 'a==0' check in your code
        with pytest.raises(ValueError):
            calc.divide(0, 5)

    # --- Advanced Operations ---
    def test_power(self):
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.get_last_result() == 8

    def test_square_root(self):
        calc = Calculator()
        assert calc.square_root(9) == 3.0

    def test_square_root_negative_raises(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.square_root(-4)

    def test_factorial(self):
        calc = Calculator()
        assert calc.factorial(5) == 120
        assert calc.factorial(0) == 1  # 0! = 1

    def test_factorial_errors(self):
        calc = Calculator()
        # Error for decimal numbers
        with pytest.raises(ValueError, match="only for integers"):
            calc.factorial(4.5)
        # Error for negative numbers
        with pytest.raises(ValueError, match="non-negative"):
            calc.factorial(-5)

    # --- Utility Functions ---
    def test_negate(self):
        calc = Calculator()
        assert calc.negate(5) == -5
        assert calc.negate(-5) == 5

    def test_absolute(self):
        calc = Calculator()
        assert calc.absolute(-10) == 10
        assert calc.absolute(5) == 5

    def test_modulo(self):
        calc = Calculator()
        assert calc.modulo(10, 3) == 1
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            calc.modulo(10, 0)

    def test_is_even(self):
        calc = Calculator()
        assert calc.is_even(4) is True
        assert calc.is_even(5) is False
        with pytest.raises(ValueError):
            calc.is_even(4.5)

    def test_gcd(self):
        calc = Calculator()
        # GCD of 12 and 15 is 3
        assert calc.gcd(12, 15) == 3
        assert calc.gcd(54, 24) == 6

    # --- Memory & Stack Tests ---
    def test_memory_store_and_clear(self):
        calc = Calculator()
        calc.memory_store(7)
        assert calc.memory_recall() == 7
        calc.memory_clear()
        assert calc.memory_recall() == 0

    def test_get_last_result_and_clear_stack(self):
        calc = Calculator()
        calc.add(1, 1)       # Stack: [2]
        calc.multiply(2, 3)  # Stack: [2, 6]
        
        # Check the last result
        assert calc.get_last_result() == 6
        
        # Get the entire stack
        assert calc.get_stack() == [2, 6]
        
        # Clear the stack
        calc.clear_stack()
        assert calc.get_stack() == []
        assert calc.get_last_result() is None
        
        # New operation after clearing
        calc.add(2, 3)
        assert calc.get_last_result() == 5