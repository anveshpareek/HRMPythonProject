from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from webdriver_manager.chrome import ChromeDriverManager


BaseUrl ="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=chrome_option)
    # webdriver.chrome(ChromeDriverManager.install(), options =chrome_option)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "HRM Test Report"
