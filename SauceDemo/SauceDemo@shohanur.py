#Web Automation Practice by @shohanur

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

def login():
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def test_menu_button():
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()

def test_all_items():
    driver.find_element(By.XPATH, "//a[@id='inventory_sidebar_link']").click()

def about():
    driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click()

def log_out():
    driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

def reset_app_state():
    driver.find_element(By.XPATH, "//a[@id='reset_sidebar_link']").click()

def back_pack():
    driver.find_element(By.XPATH,"//div[@class='inventory_item_img']").click()

def order_confirmation():
    driver.find_element(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"//button[@id='checkout']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Shohan")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Bhai")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("12345")
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "// button[ @ id = 'finish']").click()


login()
menu_button()
all_items()
about()
driver.back()
menu_button()
reset_app_state()
driver.back()
back_pack()
order_confirmation()
