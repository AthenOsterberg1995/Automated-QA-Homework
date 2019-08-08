from selenium import webdriver
import time

#basic functionality
driver = webdriver.Chrome()
driver.get("https://evereve.com/")

#I found that the program executes too fast so I added a wait time
time.sleep(5)

section = driver.find_element_by_id("mini_banner_buttonA")
section.click()

time.sleep(5)

item = driver.find_element_by_class_name("product-item-link")
item.click()

color = driver.find_element_by_id("option-label-color-166-item-8")
color.click()

size = driver.find_element_by_id("option-label-size-167-item-26")
size.click()

add_to_bag = driver.find_element_by_id("product-addtocart-button")
add_to_bag.click()

go_to_bag = driver.find_element_by_id("cart-black")
go_to_bag.click()
# driver.quit()
