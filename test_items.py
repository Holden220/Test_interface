import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser):
    browser.get(link)
    time.sleep(2)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert button, 'no item'
    browser.quit()
    


