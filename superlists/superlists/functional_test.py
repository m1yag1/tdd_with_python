
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get("http://localhost:8000")

# Sleep for 5 seconds so we can seeee
sleep(5)

try:
    assert 'Poop' in browser.title
    # Sleep for 5 seconds
    print('Passed')
except AssertionError:
    print('Failed')
finally:
    browser.close()
