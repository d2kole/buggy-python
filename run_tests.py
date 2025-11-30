#!/usr/bin/env python3
"""
Test runner script for the buggy-python project.

Usage:
    python3 run_tests.py              # Run all tests
    python3 run_tests.py -v           # Run with verbose output
    python3 run_tests.py test_loop    # Run specific test module
"""

import sys
import unittest

if __name__ == '__main__':
    # Discover and run all tests in the tests directory
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Run with verbosity level 2 for detailed output
    verbosity = 2 if '-v' in sys.argv or '--verbose' in sys.argv else 1
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)