from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

options = uc.ChromeOptions()
options.add_argument('--incognito')
driver = uc.Chrome(options=options)

driver.get("https://scrap.tf/login")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]')))
login_box = driver.find_element(By.XPATH, '//input[@type="text"]')
password_box = driver.find_element(By.XPATH, '//input[@type="password"]')

login_box.send_keys("Hwhdbdbsnso")
password_box.send_keys("84H$DUjshdb9282")
time.sleep(2)

signin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'newlogindialog_SubmitButton_2QgFE')))
signin_button.click()
time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'imageLogin')))
signin_button2 = driver.find_element(By.ID, 'imageLogin')
signin_button2.click()
time.sleep(2)

driver.get("https://scrap.tf/raffles")
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.raffle-name a")))

raffle_links = driver.find_elements(By.CSS_SELECTOR, "div.raffle-name a")
main_window = driver.current_window_handle

for raffle_link in raffle_links:
    ActionChains(driver).key_down(Keys.CONTROL).click(raffle_link).key_up(Keys.CONTROL).perform()
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
    new_window = [window for window in driver.window_handles if window != main_window][-1]
    driver.switch_to.window(new_window)
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Enter Raffle')]")))
    enter_raffle_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Enter Raffle')]")
    driver.execute_script("arguments[0].click();", enter_raffle_button)
    time.sleep(2)
    
    driver.close()
    driver.switch_to.window(main_window)
    time.sleep(1)
