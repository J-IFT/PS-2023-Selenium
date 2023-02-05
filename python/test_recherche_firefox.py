import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WelcomePage:
    ''' A Page Object to model the welcome page of Wikipedia '''

    title = "Wikipedia, l’encyclopédie libre"
    url = "https://fr.wikipedia.org/"
    

    def __init__(self, driver):
        self.driver = driver
        self.query_field = WelcomePage.QueryField(driver)

    def go(self):
        print("going to : ", WelcomePage.url)
        self.driver.get(WelcomePage.url)
        return self

    def get_title(self):
        title = self.driver.title
        print("title : ", title)
        return title

    def search(self, query):
        print("search : ", query)
        self.query_field.clear().search(query)
        return self

    def has_results(self):
        return "No results found." not in self.driver.page_source

    class QueryField:
        ''' A Page Element to model the query field of the welcome page '''

        def __init__(self, driver):
            self.driver = driver

        def __get_elem(self):
            if not hasattr(self, 'elem'):
                self.elem = self.driver.find_element(By.CSS_SELECTOR, "[name='q']")
            return self.elem

        def clear(self):
            self.__get_elem().clear()
            return self

        def search(self, query):
            input = self.__get_elem()
            input.send_keys("pycon")
            input.send_keys(Keys.RETURN)
            return self

class PythonOrgSearch(unittest.TestCase):
    ''' A test class '''

    def setUp(self):
        ''' Executed before each test '''
        self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            options=webdriver.FirefoxOptions())

    def tearDown(self):
        ''' Executed after each test '''
        self.driver.close()

    def test_testrecherchefirefox(self):
        self.driver.get("https://fr.wikipedia.org/wiki/Wiki")
        self.driver.set_window_size(1280, 720)
        time.sleep(1)
        self.driver.find_element(By.ID, "searchInput").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "search").send_keys("François Hollande")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cdx-button").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "searchInput").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "search").send_keys("emmanuel macron")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cdx-button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "search").send_keys("jacques chirac")
        time.sleep(1)
        self.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)

if __name__ == "__main__":
    unittest.main()
