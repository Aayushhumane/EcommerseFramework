import pytest
from selenium import webdriver
import pytest_metadata
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("launching Chrome Browser")
        driver=webdriver.Chrome()

    elif browser=="firefox":
        print('Launching firefox Browser')
        driver= webdriver.Firefox()


    else:
        print('launching default browser')
        driver= webdriver.Chrome()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############# HTML Report ############

# def pytest_configure(config):
#     config._metadata['Project Name'] ='EcommerseFramework'
#     config._metadata['Module Name'] ='customer'
#     config._metadata['Taster Name'] ='Aayush'
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME",None)
#     metadata.pop("Plugins",None)
