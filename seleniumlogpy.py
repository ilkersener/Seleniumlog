import time

import selenium.webdriver as webdriver

browser = webdriver.Chrome()

browser.get("https://www.instagram.com")


time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("Your Username")
password.send_keys("Your Password")

login = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")
login.click()

browser.get("https://www.facebook.com/")

email = browser.find_element_by_name("email")
password3 = browser.find_element_by_name("pass")

email.send_keys("Your E-mail")
password3.send_keys("Your Password")

login4 = browser.find_element_by_xpath("//*[@id='u_0_b']")
login4.click()

browser.get("https://www.linkedin.com/login/tr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email2 = browser.find_element_by_name("session_key")
password4 = browser.find_element_by_name("session_password")

email2.send_keys("Your E-Mail")
password4.send_keys("Your Password")

login5 = browser.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button")
login5.click()

browser.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

mail = browser.find_element_by_xpath("//*[@id='identifierId']")
mail.send_keys("Your E-Mail")

login2 = browser.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]")
login2.click()

password2 = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
password2.send_keys("Your Password")

login3 = browser.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]")
login3.click()
