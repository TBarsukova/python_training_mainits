import json
import os.path

import pytest

from fixture.application import Application


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target

@pytest.fixture(scope = "session")
def app(request):
    global fixture 
    global target
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        config = load_config(request.config.getoption("--target"))
        fixture = Application(browser=browser, url=config['web']['baseUrl'])
    fixture.session.ensure_login(username=config['webadmin']['username'], password=config['webadmin']['password'])
    return fixture
    

@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        global fixture 
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")