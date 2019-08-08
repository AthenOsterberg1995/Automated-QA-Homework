#selenium is the autometed testing framework
from selenium import webdriver

#Test opens the home page
try:
    driver = webdriver.Chrome()
    driver.get("https://evereve.com/")
except:
    print("webdriver is missing")

#Test looks for a section to shop through    
try:
    section = driver.find_element_by_id("mini_banner_buttonA")
    section.click()
except:
    print("Element for shopping section cannot be found.")

#Test looks for a product to click on
try:
    item = driver.find_element_by_class_name("product-item-link")
    item.click()
except:
    print("Element for item cannot be found.")

#Test selects a color
try:
    color = driver.find_element_by_id("option-label-color-166-item-8")
    color.click()
except:
    print("Element for color cannot be found.")

#test selects a size
try:
    size = driver.find_element_by_id("option-label-size-167-item-26")
    size.click()
except:
    print("Element for size cannot be found.")

#test adds the item to the bag
try:
    add_to_bag = driver.find_element_by_id("product-addtocart-button")
    add_to_bag.click()
except:
    print("Element for adding item to bag cannot be found or not all fields are selected.")

#test goes to the bag
try:
    go_to_bag = driver.find_element_by_id("cart-black")
    go_to_bag.click()
except:
    print("Element for going to the bag cannot be found")

#I checked to see if the test would fail by commenting out add_to_bag.click()
#to make sure it would fail with an empty bag.
#Test checks for something in the bag
try:
    check_full = driver.find_element_by_class_name("action.primary.checkout")
    print("Item added.")
except:
    print("Item not added")
    
driver.quit()
