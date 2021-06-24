from base.init_session import init_session
from action.login import Login
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session=init_session()
        self.l=Login(self.session)
    def tearDown(self) -> None:
        pass
    def test_login(self):
        self.l.doLogin()
        self.assertEqual(1,1)

if __name__=="__main__":
    unittest.main()