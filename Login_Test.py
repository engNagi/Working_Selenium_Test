from selenium import webdriver
import unittest
from HomePage import HomePage
from LoginPage import LoginPage


class LoginTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	def test_login_valid(self):
		driver = self.driver
		driver.get("https://opensource-demo.orangehrmlive.com/")

		login = LoginPage(driver)
		login.enter_username("Admin")
		login.enter_password("admin123")
		login.click_login()

		homepage = HomePage(driver)
		homepage.click_welcome()

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Completed")


if __name__ == '__main__':
	unittest.main()