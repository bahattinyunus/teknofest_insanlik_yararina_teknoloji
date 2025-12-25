import unittest
import sys
import os

# Add src to the path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from utils import get_timestamp
except ImportError:
    # Handle the case where src is not yet fully populated or import fails
    get_timestamp = None

class TestBasicSystem(unittest.TestCase):

    def test_environment_setup(self):
        """
        Verify that the testing environment is correctly set up.
        """
        self.assertTrue(True)

    def test_utils_import(self):
        """
        Verify that we can import utilities from src.
        """
        self.assertIsNotNone(get_timestamp, "Could not import get_timestamp from utils")
        if get_timestamp:
            ts = get_timestamp()
            self.assertIsInstance(ts, str)
            self.assertTrue(len(ts) > 0)

if __name__ == '__main__':
    unittest.main()
