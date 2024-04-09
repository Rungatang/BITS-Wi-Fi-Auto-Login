from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import configparser

def login_to_wifi(config):
    driver = webdriver.Chrome()
    driver.get(config['WiFi']['login_url'])
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(config['WiFi']['username'])
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(config['WiFi']['password'])
    login_button = driver.find_element(By.ID, 'loginbtn')
    login_button.click()
    driver.implicitly_wait(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    msg_div = soup.find('div', id='msgDiv')
    if msg_div and config['WiFi']['username'] in msg_div.text:
        print(f"Successfully logged in as {config['WiFi']['username']}.")
    else:
        print("Failed to log in.")

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    login_to_wifi(config)