from selenium import webdriver
import unittest

#x = webdriver.Firefox()
#x.get('localhost:8000')

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
#        self.browser = implicitly_wait()
    def tearDown(self):
        self.browser.quit()
    def test_startlist(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()


