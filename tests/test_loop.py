"""
Unit tests for snippets/loop.py

This test suite provides comprehensive coverage for the lambda_array function,
including happy paths, edge cases, and the lambda closure behavior that is
characteristic of Python.
"""

import unittest
import sys
import os

# Add parent directory to path to import snippets module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestLambdaArray(unittest.TestCase):
    """Test suite for the lambda_array function"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        # Import here to ensure fresh import for each test
        from snippets.loop import lambda_array
        self.lambda_array_func = lambda_array

    def test_lambda_array_returns_list(self):
        """Test that lambda_array returns a list (not dict or other type)"""
        result = self.lambda_array_func()
        self.assertIsInstance(result, list, "lambda_array should return a list")

    def test_lambda_array_length(self):
        """Test that lambda_array returns exactly 10 lambda functions"""
        result = self.lambda_array_func()
        self.assertEqual(len(result), 10, "lambda_array should contain 10 elements")

    def test_lambda_array_contains_callables(self):
        """Test that all elements in the returned array are callable (functions)"""
        result = self.lambda_array_func()
        for i, func in enumerate(result):
            with self.subTest(index=i):
                self.assertTrue(callable(func), f"Element at index {i} should be callable")

    def test_lambda_closure_behavior(self):
        """
        Test the lambda closure behavior - a classic Python gotcha.
        
        Due to late binding in Python closures, all lambdas will reference the same 'i'
        which will have the value 9 (the last value in range(10)) after the loop completes.
        
        This is the expected behavior and the test in main.py relies on this:
        lambdas[0](10) should equal 19 (which is 10 + 9)
        """
        result = self.lambda_array_func()
        
        # All lambdas should add 9 (the final value of i) to their input
        for i, func in enumerate(result):
            with self.subTest(index=i):
                # Each lambda should add 9 to the input
                self.assertEqual(func(10), 19, f"lambda[{i}](10) should equal 19")
                self.assertEqual(func(0), 9, f"lambda[{i}](0) should equal 9")
                self.assertEqual(func(5), 14, f"lambda[{i}](5) should equal 14")

    def test_main_py_assertion(self):
        """Test the specific assertion from main.py: lambdas[0](10) == 19"""
        result = self.lambda_array_func()
        self.assertEqual(result[0](10), 19, "lambdas[0](10) should equal 19")

    def test_lambda_with_zero(self):
        """Test lambda functions with zero as input"""
        result = self.lambda_array_func()
        # All should return 9 (0 + 9)
        self.assertEqual(result[0](0), 9)
        self.assertEqual(result[5](0), 9)
        self.assertEqual(result[9](0), 9)

    def test_lambda_with_negative_numbers(self):
        """Test lambda functions with negative input values"""
        result = self.lambda_array_func()
        self.assertEqual(result[0](-5), 4, "lambda(0)(-5) should equal 4 (9 - 5)")
        self.assertEqual(result[0](-10), -1, "lambda(0)(-10) should equal -1 (9 - 10)")

    def test_lambda_with_large_numbers(self):
        """Test lambda functions with large input values"""
        result = self.lambda_array_func()
        self.assertEqual(result[0](1000), 1009, "lambda(0)(1000) should equal 1009")
        self.assertEqual(result[0](999999), 1000008, "lambda(0)(999999) should equal 1000008")

    def test_lambda_with_floats(self):
        """Test lambda functions with floating-point input values"""
        result = self.lambda_array_func()
        self.assertAlmostEqual(result[0](10.5), 19.5, places=7)
        self.assertAlmostEqual(result[0](3.14159), 12.14159, places=7)

    def test_all_lambdas_identical_behavior(self):
        """
        Test that all lambdas in the array exhibit identical behavior
        due to the closure capturing the final value of i
        """
        result = self.lambda_array_func()
        test_values = [0, 1, 5, 10, -5, 100, 3.5]
        
        for test_val in test_values:
            with self.subTest(test_value=test_val):
                # Get the result from the first lambda
                expected = result[0](test_val)
                
                # All other lambdas should return the same value
                for i in range(1, len(result)):
                    actual = result[i](test_val)
                    self.assertEqual(actual, expected, 
                                   f"lambda[{i}]({test_val}) should equal lambda[0]({test_val})")

    def test_lambda_array_returns_new_list_each_call(self):
        """Test that calling lambda_array multiple times returns different list objects"""
        result1 = self.lambda_array_func()
        result2 = self.lambda_array_func()
        
        # Should be different list objects
        self.assertIsNot(result1, result2, "Each call should return a new list object")
        
        # But should have the same length
        self.assertEqual(len(result1), len(result2), "Both lists should have same length")

    def test_lambda_return_values_are_numeric(self):
        """Test that lambda functions return numeric values when given numeric input"""
        result = self.lambda_array_func()
        output = result[0](10)
        self.assertIsInstance(output, (int, float), "Lambda should return a numeric value")

    def test_lambda_with_boundary_values(self):
        """Test lambda functions with boundary values"""
        result = self.lambda_array_func()
        
        # Test with very small and very large values
        test_cases = [
            (0, 9),           # zero
            (1, 10),          # one
            (-1, 8),          # negative one
            (sys.maxsize, sys.maxsize + 9),  # max int
            (-sys.maxsize, -sys.maxsize + 9), # min int
        ]
        
        for input_val, expected in test_cases:
            with self.subTest(input=input_val):
                self.assertEqual(result[0](input_val), expected)

    def test_function_can_be_called_multiple_times(self):
        """Test that each lambda can be called multiple times with consistent results"""
        result = self.lambda_array_func()
        lambda_func = result[0]
        
        # Call the same lambda multiple times
        first_call = lambda_func(10)
        second_call = lambda_func(10)
        third_call = lambda_func(10)
        
        self.assertEqual(first_call, second_call)
        self.assertEqual(second_call, third_call)
        self.assertEqual(first_call, 19)

    def test_lambda_array_empty_before_loop(self):
        """
        Test that verifies the function initializes an empty array.
        This is more of a design verification test.
        """
        result = self.lambda_array_func()
        # Should have exactly 10 elements (not 0, not more than 10)
        self.assertEqual(len(result), 10)

    def test_specific_index_access(self):
        """Test accessing specific indices in the returned lambda array"""
        result = self.lambda_array_func()
        
        # Test first element
        self.assertEqual(result[0](10), 19, "First lambda should work correctly")
        
        # Test middle element
        self.assertEqual(result[4](10), 19, "Middle lambda should work correctly")
        
        # Test last element
        self.assertEqual(result[9](10), 19, "Last lambda should work correctly")

    def test_lambda_with_string_concatenation_attempt(self):
        """
        Test edge case: what happens when lambda is called with a string?
        Since the lambda does x + i where i is an integer, passing a string 
        will attempt string + int which should raise TypeError.
        """
        result = self.lambda_array_func()
        
        with self.assertRaises(TypeError):
            result[0]("string")

    def test_lambda_preserves_input_type_when_appropriate(self):
        """Test that lambda preserves input type for numeric operations"""
        result = self.lambda_array_func()
        
        # Integer input should give integer output
        int_result = result[0](10)
        self.assertIsInstance(int_result, int)
        
        # Float input should give float output
        float_result = result[0](10.0)
        self.assertIsInstance(float_result, float)


class TestLambdaArrayEdgeCases(unittest.TestCase):
    """Additional edge case tests for lambda_array"""

    def setUp(self):
        """Set up test fixtures"""
        from snippets.loop import lambda_array
        self.lambda_array_func = lambda_array

    def test_consecutive_calls_independent(self):
        """Test that consecutive calls to lambda_array are independent"""
        result1 = self.lambda_array_func()
        result2 = self.lambda_array_func()
        
        # Modify one (by calling it) shouldn't affect the other
        val1 = result1[0](5)
        val2 = result2[0](5)
        
        self.assertEqual(val1, val2, "Results should be independent")

    def test_lambda_mathematical_properties(self):
        """Test mathematical properties of the lambda functions"""
        result = self.lambda_array_func()
        
        # Commutativity test: f(a) + b == f(a + b) - b for addition
        a, b = 10, 5
        lambda_result = result[0](a)
        
        # Since lambda does x + 9, we expect: (10 + 9) == 19
        self.assertEqual(lambda_result, 19)
        
        # Test associativity
        self.assertEqual(result[0](10), result[0](5 + 5))
        self.assertEqual(result[0](10), result[0](8 + 2))

    def test_all_ten_lambdas_exist(self):
        """Explicitly test that all 10 expected lambdas exist and are accessible"""
        result = self.lambda_array_func()
        
        # Test each index from 0 to 9
        for i in range(10):
            with self.subTest(index=i):
                self.assertIsNotNone(result[i], f"Lambda at index {i} should exist")
                self.assertTrue(callable(result[i]), f"Lambda at index {i} should be callable")
                # Verify it works
                self.assertEqual(result[i](10), 19, f"Lambda at index {i} should compute correctly")

    def test_lambda_none_input(self):
        """Test behavior when None is passed to lambda (should raise TypeError)"""
        result = self.lambda_array_func()
        
        with self.assertRaises(TypeError):
            result[0](None)

    def test_closure_captures_final_iteration_value(self):
        """
        Explicitly test that the closure captures the final iteration value (9).
        
        This is a critical test that verifies the 'late binding' behavior of
        Python closures, which is the reason lambdas[0](10) == 19 and not 10.
        """
        result = self.lambda_array_func()
        
        # The loop goes: for i in range(10), so i takes values 0, 1, 2, ..., 9
        # After the loop, i has the value 9
        # All lambdas capture this final value due to late binding
        
        # Therefore, all lambdas should add 9 to their input
        for idx in range(10):
            with self.subTest(lambda_index=idx):
                # Testing with input 0 makes it clear we're adding 9
                self.assertEqual(result[idx](0), 9, 
                               f"Lambda {idx} should add 9 to input (closure captured final i=9)")


class TestLambdaArrayIntegration(unittest.TestCase):
    """Integration tests that mirror the usage in main.py"""

    def test_main_py_usage_pattern(self):
        """Test the exact usage pattern from main.py"""
        from snippets.loop import lambda_array
        
        # Replicate main.py usage
        lambdas = lambda_array()
        
        # The assertion from main.py
        self.assertEqual(lambdas[0](10), 19, "lambdas[0](10) should equal 19")
        
        # Additional verification
        self.assertIsInstance(lambdas, list)
        self.assertEqual(len(lambdas), 10)

    def test_practical_usage_scenarios(self):
        """Test practical usage scenarios for the lambda array"""
        from snippets.loop import lambda_array
        
        lambdas = lambda_array()
        
        # Scenario 1: Using lambdas in a map operation
        inputs = [1, 2, 3, 4, 5]
        results = [lambdas[0](x) for x in inputs]
        expected = [10, 11, 12, 13, 14]  # Each input + 9
        self.assertEqual(results, expected)
        
        # Scenario 2: Using different lambdas (though they're all the same)
        self.assertEqual(lambdas[5](20), 29)
        self.assertEqual(lambdas[9](100), 109)

    def test_lambda_array_in_list_comprehension(self):
        """Test using lambda_array results in list comprehensions"""
        from snippets.loop import lambda_array
        
        lambdas = lambda_array()
        
        # Apply all lambdas to the same value
        results = [func(5) for func in lambdas]
        
        # All should return 14 (5 + 9)
        expected = [14] * 10
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)