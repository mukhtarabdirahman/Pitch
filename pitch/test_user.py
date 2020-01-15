import unittest
from models import User,Post

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_post = Post()
        self.new_comment = Comment()
    def test_user_instance(self):
        pass
    def test_post_instance(self):
        pass
    
class TestPost(unittest.TestCase):
    def setUp(self):
        self.new_post = Post()
        self.new_comment = Comment()
    def test_user_instance(self):
        pass
    def test_post_instance(self):
        pass

if __name__ == '__main__':
    unittest.main()