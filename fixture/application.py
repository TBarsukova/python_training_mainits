from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self, browser, url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecoginzed browser: {browser}")
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.url = url

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
