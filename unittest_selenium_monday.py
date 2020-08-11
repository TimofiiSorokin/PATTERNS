import unittest

from selenium import webdriver


class Monday(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://vaisible.monday.com/users/sign_in')

    def test_login(self):
        self.driver.find_element_by_id("user_email").send_keys("timofii.sorokin@vaisible.com")
        self.driver.find_element_by_id("user_password").send_keys("qweasdzxc1234")
        self.driver.find_element_by_class_name("ladda-label").click()

        self.driver.get('https://vaisible.monday.com/admin/free-plan/overview')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
