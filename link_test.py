import unittest
from selenium import webdriver
class LinkTest (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def test_link(self):
        driver = self.driver
        driver.get("http://blog.csssr.ru/qa-engineer/")
        driver.find_element_by_xpath("//a[contains(text(),'НАХОДИТЬ НЕСОВЕРШЕНСТВА')]").click()
        href = driver.find_element_by_xpath("//a[contains(text(),'Софт для быстрого создания скриншотов')]").get_attribute('href')
        assert(href == "http://monosnap.com/")


if __name__ == "__main__":
    unittest.main()