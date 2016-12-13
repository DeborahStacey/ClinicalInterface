import unittest
import middleware

class TestStringMethods(unittest.TestCase):

    def test_checkDateTrue(self):
        print("Testing Checkdate True")
        # True case
        self.assertTrue(middleware.checkDate('2016-04-03'))

    def test_checkDateFalse(self):
        print("Testing Checkdate False")
        # False case
        self.assertFalse(middleware.checkDate('s-04,asda'))        

    def test_sendJsonTrue(self):
        print("Testing sendJson/sendData True")
        message = middleware.convertJson("tansari.json") 
        # True case        
        self.assertTrue(middleware.sendJson(message,"update"))

    def test_sendJsonFalse(self):
        print("Testing sendJson/sendData False")
        message = middleware.convertJson("temp.json") 
        # False cases
        self.assertFalse(middleware.sendJson(message,"add"))        

    def test_loginTrue(self):
        print("Testing Login True")
        # True case
        userEmail = "taha@mymail.com"
        password = "soccer123"
        self.assertTrue(middleware.mockLogin(userEmail, password))
        
    def test_loginFalse(self):
        # False case
        userEmail = "sadoiadoia"
        password = "aaaaaasa2_!aaaa"
        self.assertFalse(middleware.mockLogin(userEmail, password))        

if __name__ == '__main__':
    print("Note: Internet connection required to run these tests")
    unittest.main()