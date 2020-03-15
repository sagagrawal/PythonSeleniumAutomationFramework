import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.Log import Log


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--headless", action="store", default="False"
    )
    parser.addoption(
        "--url", action="store", default=None
    )


@pytest.fixture(scope="class")
def setup(request):
    log = Log("runLogs.txt")
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    url = request.config.getoption("url")

    log.debug(f"{browser_name} will be used to perform the Tests.")
    log.debug(f"{headless} is the value for Headless")

    if browser_name == "chrome":
        chrome_options = Options()
        if headless.lower() == "true":
            log.info("Browser will run in headless mode")
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=r"C:\geckodriver.exe")
    else:
        log.error(f"{browser_name} driver binary path is not known to the Framework.")

    if url is not None:
        driver.get(url)
        driver.maximize_window()

    request.cls.log = log
    request.cls.driver = driver
    yield
    driver.close()

