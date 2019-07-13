from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the user')
msg = input('Enter the message that you want to send')
count = int(input('Enter the count'))

input("Enter any key after scanning QR Code")

textbox = driver.find_element_by_class_name('_2zCfw')
textbox.send_keys(name)
textbox.send_keys('\n')

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()

driver.close()
