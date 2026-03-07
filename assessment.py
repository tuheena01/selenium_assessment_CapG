from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(opts)
#
#
#
#
# ##########################first questions##########################################
# # # driver=webdriver.Chrome(opts)
# # #
# # # driver.get('https://demowebshop.tricentis.com/')
# # #
# # # book=driver.find_element('xpath',"(//a[contains(text(),'Books')])[1]").click()
# # #
# # # time.sleep(2)
# # #
# # # driver.find_element('xpath',"(//a[contains(text(),'Computing and Internet')])[1]").click()
# # # time.sleep(2)
# # #
# # # driver.find_element('xpath','//input[@id="add-to-cart-button-13"]').click()
# # # time.sleep(2)
# # #
# # #
# # # driver.find_element('xpath',"//a[contains(text(),'shopping cart')]").click()
# # #
# # # time.sleep(2)
# #
# #
# # #########################second question##############################
# #
# # driver=webdriver.Chrome(opts)
# # driver.get('https://demowebshop.tricentis.com/')
# # time.sleep(2)
# #
# # driver.find_element('xpath',"(//a[contains(text(),'Electronics')])[1]").click()
# # time.sleep(2)
# #
# # driver.find_element('xpath','//img[@alt="Picture for category Cell phones"]').click()
# # time.sleep(2)
#
#
# ##################third question#####################################
#
# # driver = webdriver.Chrome()
# # driver.maximize_window()
# #
# # driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# #
# # driver.find_element('xpath',"//button[text()='Start']").click()
# #
# # wait = WebDriverWait(driver, 10)
# # hello_text = wait.until(
# #     EC.visibility_of_element_located(('xpath', "//h4[text()='Hello World!']"))
# # )
# #
# # print(hello_text.text)
#
#
# #####################four question####################################
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # driver=webdriver.Chrome(options=opts)
# # driver.get('https://the-internet.herokuapp.com/dynamic_controls')
# #
# #
# # time.sleep(2)
# # wait_obj = WebDriverWait(driver, 20)
# # driver.find_element('xpath',"//button[text()='Remove']").click()
# # time.sleep(2)
# #
# # wait_obj.until(EC.visibility_of_element_located(('xpath', "//button[text()='Add']")))
# #
# # driver.find_element('xpath',"//button[text()='Add']").click()
# # time.sleep(2)
#
#
#
# ###########################five question##############################
#
# # driver.get('https://demoqa.com/select-menu')
# # time.sleep(2)
# #
# # list2=driver.find_element('xpath','(//div[@class="css-19bb58m"])[1]').click()
# # select_obj = Select(list2)
# # select_obj.select_by_value("Group 2, option 1")
# # time.sleep(2)
#
#
# ################################qstn 6 ###################################################
#
# # driver.get('https://demoqa.com/select-menu')
# # time.sleep(2)
# # element = driver.find_element("xpath", "//select[@id='cars']")
# # select_obj = Select(element)
# #
# # select_obj.select_by_index(0)
# # select_obj.select_by_index(1)
# # select_obj.select_by_index(2)
# #
# # time.sleep(2)
# #
# # selected_options = select_obj.all_selected_options
# #
# # print("Selected options are:")
# # for option in selected_options:
# #     print(option.text)
#
# #time.sleep(3)
#
#
#
# ##############################qstn 7 ########################################
# #
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option('detach', True)
# #
# # driver = webdriver.Chrome(options=opts)
# # driver.get("https://demoqa.com/menu/")
# #
# # driver.maximize_window()
# # time.sleep(2)
# #
# # ac = ActionChains(driver)
# #
# # main_item = driver.find_element('xpath', "//a[text()='Main Item 2']")
# # ac.move_to_element(main_item).perform()
# # time.sleep(2)
# #
# # sub_sub_list = driver.find_element('xpath', "//a[text()='SUB SUB LIST »']")
# # ac.move_to_element(sub_sub_list).perform()
# # time.sleep(2)
# #
# # sub_sub_item1 = driver.find_element('xpath', "//a[text()='Sub Sub Item 1']")
# # sub_sub_item1.click()
# #
# # time.sleep(2)
#
#
# #########################eight question################################
#
#
#
# driver.get("https://demoqa.com/droppable")
# time.sleep(2)
#
#
# drag_element = driver.find_element('id', "draggable")
# drop_element = driver.find_element('id', "droppable")
#
# actions = ActionChains(driver)
# actions.drag_and_drop(drag_element, drop_element).perform()
#
# time.sleep(2)
#
# result_text = drop_element.text
#
# if result_text == "Dropped!":
#     print("Drag and Drop Successful")
# else:
#     print("Drag and Drop Failed")
#
#
#############################nine questions##############################



# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
#
# driver = webdriver.Chrome(options=opts)
# driver.maximize_window()
#
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
#
# driver.find_element('xpath', "//button[text()='Click for JS Confirm']").click()
#
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
#
# time.sleep(2)
# result = driver.find_element('id', "result").text
#
# if result == "You clicked: Ok":
#     print("Alert handled successfully")
# else:
#     print("Alert handling failed")


############################ten question ###########################

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=opts)
# driver.maximize_window()
#
#
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(2)
#
#
# driver.find_element('xpath', "//a[contains(text(),'Books')]").click()
# time.sleep(2)
#
# books = driver.find_elements('xpath', "//div[@class='product-item']")
#
# for book in books:
#     price_text = book.find_element('xpath', '//span[@class="price actual-price"]').text
#     price = float(price_text.replace("$", ""))
#     if price < 20:
#         book.find_element('xpath', ".//input[@value='Add to cart']").click()
#         print("Book added with price:", price)
#
# time.sleep(3)



##########################syntax#################################
""""
    Write the syntax for the xpath to locate the elements using
	*	attributes
	*	text
	*	group indexing
	*	contains
"""

#ATTRIBUTE : //tagname[@attribute='value']
#TEXT : //tagname[text()='text_value']
#group indexing : (xpath_expression)[index] - example: (//input[@type='text'])[2]
#contains : //tagname[contains(@attribute,'partial_value')]




















