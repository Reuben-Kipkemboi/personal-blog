import unittest
from app.models import Blogs

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blogs(
            "Software Engineering.",
            "The act of making computer softwares can be traced wayback in the early 19th century.",
            "Reuby Studios"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blogs))

if __name__ == "__main__":
    unittest.main()