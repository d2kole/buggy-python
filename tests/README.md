# Test Suite for buggy-python

## Overview

This directory contains comprehensive unit tests for the buggy-python project, with a primary focus on testing the `snippets/loop.py` module.

## Test Coverage

### `test_loop.py`

Comprehensive test suite for the `lambda_array()` function with 25+ test cases covering:

#### Basic Functionality Tests
- **test_lambda_array_returns_list**: Verifies return type is a list
- **test_lambda_array_length**: Ensures exactly 10 lambda functions are returned
- **test_lambda_array_contains_callables**: Validates all elements are callable functions

#### Lambda Closure Behavior Tests
- **test_lambda_closure_behavior**: Tests Python's late binding in closures (critical!)
- **test_closure_captures_final_iteration_value**: Explicitly verifies closure captures i=9
- **test_all_lambdas_identical_behavior**: Confirms all lambdas behave identically

#### Main.py Integration Tests
- **test_main_py_assertion**: Tests the specific assertion `lambdas[0](10) == 19`
- **test_main_py_usage_pattern**: Replicates exact usage from main.py

#### Edge Cases & Input Validation
- **test_lambda_with_zero**: Tests with zero input
- **test_lambda_with_negative_numbers**: Tests with negative values
- **test_lambda_with_large_numbers**: Tests with large integers
- **test_lambda_with_floats**: Tests with floating-point numbers
- **test_lambda_with_boundary_values**: Tests with sys.maxsize and edge values
- **test_lambda_with_string_concatenation_attempt**: Tests TypeError on invalid input
- **test_lambda_none_input**: Tests behavior with None input

#### Behavioral & Design Tests
- **test_lambda_array_returns_new_list_each_call**: Verifies independence of calls
- **test_function_can_be_called_multiple_times**: Tests idempotency
- **test_lambda_preserves_input_type_when_appropriate**: Tests type preservation
- **test_specific_index_access**: Tests accessing different indices
- **test_all_ten_lambdas_exist**: Verifies all 10 lambdas are accessible

#### Mathematical Properties Tests
- **test_lambda_mathematical_properties**: Tests mathematical correctness
- **test_lambda_return_values_are_numeric**: Ensures numeric return types

#### Practical Usage Tests
- **test_practical_usage_scenarios**: Tests real-world usage patterns
- **test_lambda_array_in_list_comprehension**: Tests usage in comprehensions

## Running the Tests

### From Repository Root

```bash
# Run all tests with standard output
python3 -m unittest discover tests

# Run all tests with verbose output
python3 -m unittest discover tests -v

# Run specific test file
python3 -m unittest tests.test_loop

# Run specific test class
python3 -m unittest tests.test_loop.TestLambdaArray

# Run specific test method
python3 -m unittest tests.test_loop.TestLambdaArray.test_main_py_assertion
```

### Using the Test Runner Script

```bash
# Run all tests
python3 run_tests.py

# Run with verbose output
python3 run_tests.py -v
```

### From Tests Directory

```bash
cd tests
python3 -m unittest test_loop -v
```

## Understanding the Lambda Closure Gotcha

The tests extensively cover Python's **late binding closure behavior**, which is a common gotcha:

```python
# The bug: All lambdas capture the same 'i' reference
lambda_methods = []
for i in range(10):
    lambda_methods.append(lambda x: x + i)
# After the loop, i = 9, so ALL lambdas add 9!

# Therefore:
lambdas[0](10) == 19  # Not 10! (10 + 9, not 10 + 0)
lambdas[5](10) == 19  # Also 19! (10 + 9, not 10 + 5)
```

This is intentional in the project and the tests verify this behavior extensively.

## Test Structure

The test suite is organized into three test classes:

1. **TestLambdaArray**: Core functionality and behavior tests
2. **TestLambdaArrayEdgeCases**: Edge cases and boundary conditions
3. **TestLambdaArrayIntegration**: Integration tests matching main.py usage

## Expected Test Results

When the bugs in `loop.py` are **fixed**, all tests should **PASS**.

Current bugs in `loop.py` (as of the current branch):
1. Line 11: `for i in 10:` → should be `for i in range(10):`
2. Line 13: `lambdamethods` → should be `lambda_methods` (with underscore)
3. Line 13: `.push()` → should be `.append()` (Python, not JavaScript)
4. Line 13: `lambda x: x + n` → should be `lambda x: x + i` (n is undefined)

## Adding More Tests

To add more tests:

1. Add new test methods to existing test classes, or
2. Create a new test class inheriting from `unittest.TestCase`
3. Follow the naming convention: `test_<descriptive_name>`
4. Use `self.subTest()` for parameterized test cases
5. Add docstrings explaining what the test validates

## Test Dependencies

- **Python 3.x**: Required (standard library only)
- **unittest**: Built-in Python testing framework (no pip install needed)

No external dependencies required! All tests use Python's standard library.

## Contributing

When adding new functionality to the snippets:

1. Write tests first (TDD approach)
2. Ensure >90% code coverage
3. Test happy paths, edge cases, and error conditions
4. Add integration tests that mirror usage in main.py
5. Document any Python gotchas or tricky behavior

## Related Files

- `../main.py`: Contains assertions that these tests are based on
- `../snippets/loop.py`: The module being tested
- `../run_tests.py`: Convenient test runner script