from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import json



buffer = None
locators = {
    "Genset L1": "DK_val_181_0",
    "Genset L2": "DK_val_185_0",
    "Genset L3": "DK_val_189_0",
    "Genset L1-L2": "DK_val_205_0",
    "Genset L2-L3": "DK_val_209_0",
    "Genset L3-L1": "DK_val_213_0",
    "Genset I1": "DK_val_193_0",
    "Genset I2": "DK_val_197_0",
    "Genset I3": "DK_val_201_0",
    "Genset P Total": "DK_val_217_0",
    "Fuel level": "DK_val_247_0",
}

data = {
    "Alarm": 0,
    "Warning": 0,
    "Caution": 0,
    "Running": 0,
    "Normal": 0,
    "Silent": 0,
    "Total": 0,
    "Genset L1": "DK_val_181_0",
    "Genset L2": "DK_val_185_0",
    "Genset L3": "DK_val_189_0",
    "Genset L1-L2": "DK_val_205_0",
    "Genset L2-L3": "DK_val_209_0",
    "Genset L3-L1": "DK_val_213_0",
    "Genset I1": "DK_val_193_0",
    "Genset I2": "DK_val_197_0",
    "Genset I3": "DK_val_201_0",
    "Genset P Total": "DK_val_217_0",
    "Fuel level": "DK_val_247_0",
}

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# # driver = webdriver.Chrome(
# #     executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_options
# # )

driver = webdriver.Chrome()
action = ActionChains(driver)

BASE_URL = "https://rm.datakom.com.tr/"
user = "*******"
password = "*******"

driver.get(BASE_URL)
wait = WebDriverWait(driver, 20)

assert "Rainbow" in driver.title
usr = driver.find_element(By.ID, "Vusr")
usr.clear()
usr.send_keys(user)
pswrd = driver.find_element(By.ID, "Vpwd")
pswrd.clear()
pswrd.send_keys(password)
login = driver.find_element(By.ID, "Vlgn")
login.send_keys(Keys.RETURN)
sleep(5)

driver.find_element(By.CLASS_NAME, "dijitTreeNodeContainer").click()
sleep(1)
driver.find_element(By.ID, "DK_tree_dev_state").click()
sleep(1)
for key, val in locators.items():
    e = driver.find_element(By.CLASS_NAME, val)
    data[key] = float(e.text.lstrip()[2:-3])
e = driver.find_element(By.ID, "DK_ekran_ayak_msg_TXT").text.split(",")
for item in e:
    temp = item.split(":")
    data[temp[0]] = int(temp[1])

with open("data.json", "w") as f:
    json.dump(data, f)
