from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import csv


with open('credentials.csv', newline='') as csvfile:
	data = list(csv.reader(csvfile, delimiter=':'))


options = webdriver.FirefoxOptions()
options.set_preference('browser.link.open_newwindow', 3)
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
options.set_preference('permissions.default.stylesheet', 2)
options.set_preference('browser.link.open_newwindow.restriction', 0)
options.set_preference('browser.link.open_newwindow.override.external', -1)
options.set_preference('media.autoplay.enabled', 'false')


for lane in data:
	print ("[+] Loading browser...")
	driver = webdriver.Firefox(options=options)
	driver.get("https://www.ytmonster.net/login")
	print(f"[+] Logging In to {lane[0]} account")

	driver.find_element(By.XPATH, '//*[@id="formLogin"]/div[1]/input').send_keys(lane[0])
	driver.find_element(By.XPATH, '//*[@id="formLogin"]/div[2]/input').send_keys(lane[1])
	driver.find_element(By.XPATH, '//*[@id="formLogin"]/button').click()

	try:
		driver.find_element(By.LINK_TEXT, 'Redeem').click()
		sleep(2)
	except Exception:
		pass
	print("[+] Running the Client")
	driver.get('https://www.ytmonster.net/exchange/views')
	sleep(3)
	driver.find_element(By.ID, 'endAll').click()
	sleep(5)
	driver.get('http://ytmonster.net/client/')
	sleep(3)
	driver.find_element(By.ID, 'startBtn').click()
	sleep(3)

	print("Points:")
	print(driver.find_element(By.CLASS_NAME, 'credits').text)

print("[+] End, now sleep for 1 hour")

#driver.quit()
