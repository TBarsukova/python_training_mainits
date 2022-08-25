from selenium import webdriver
from fixture.session import SessionHelper
from fixture.soap import SoapHelper
from .project import ProjectHelper

class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecoginzed browser: {browser}")
        self.url = config['web']['baseUrl']
        self.username = config['webadmin']['username']
        self.password = config['webadmin']['password']
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)

    def destroy(self):
        self.wd.quit()
