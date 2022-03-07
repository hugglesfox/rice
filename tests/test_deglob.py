import unittest
from rice.utils import deglob


class TestDeglobMethod(unittest.TestCase):
    def test_deglob(self):
        paths = ["rice/*.py", "tests/*.py"]
        self.assertTrue(
            "rice/__init__.py" in deglob(paths) and "tests/__init__.py" in deglob(paths)
        )
