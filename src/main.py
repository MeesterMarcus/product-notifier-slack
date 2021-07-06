from selenium_driver import driver
from slack_client import client
import time

url = "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card" \
      "/6432400.p?skuId=6432400 "
driver.get(url)


def is_available_text(driver):
    e = driver.find_element_by_css_selector('.fulfillment-add-to-cart-button > div > div > button')
    return e.text


def check_website():
    print('refreshing...')
    driver.refresh()
    try:
        available_text = is_available_text(driver)
        if available_text == 'Sold Out':
            message = 'Product Sold Out: \n' + url
        else:
            message = '<@U027KMC0S57> Product In Stock: \n' + url
            client.chat_postMessage(channel='#bottest1', text=message)
    except Exception as e:
        message = str(e)

    print('Message: ' + message)


while True:
    check_website()
    # This used to run every 5 minutes.
    # I modified it to run every 60 minutes.
    waited = 0
    for i in range(60):
        time.sleep(60)
        waited += 1
        print(f'waited for: {waited} minute')
