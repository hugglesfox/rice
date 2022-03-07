import os
import unittest
from rice.utils import template


class TestTemplateMethod(unittest.TestCase):
    def setUp(self):
        os.environ["RICE_TEST"] = "Test"

        with open("test.html", "w") as fp:
            fp.write("<h1>Hello {{ RICE_TEST }}</h1>")
        with open("test.yaml", "w") as fp:
            fp.write("user: '{{ RICE_TEST }}'")

    def test_template(self):
        template(["test.html", "test.yaml"])

        with open("test.html") as fp:
            self.assertEqual(fp.read(), "<h1>Hello Test</h1>")
        with open("test.yaml") as fp:
            self.assertEqual(fp.read(), "user: 'Test'")

    def tearDown(self):
        del os.environ["RICE_TEST"]
        os.remove("test.html")
        os.remove("test.yaml")
