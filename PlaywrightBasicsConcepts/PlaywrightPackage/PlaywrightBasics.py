import re
from playwright.sync_api import sync_playwright,expect
def validate_title():
    with sync_playwright() as p:
        browser=p.chromium.launch(channel="chrome",headless=False)
        page=browser.new_page()
        page.goto("https://demo.nopcommerce.com/")
        expect(page).to_have_title(re.compile("nopCommerce *"))
        print("Test Passed")
        browser.close()
def register():
    with sync_playwright() as p:
        browser=p.chromium.launch(channel="chrome",headless=False)
        page=browser.new_page()
        page.goto("https://demo.nopcommerce.com/")
        page.wait_for_timeout(5000)
        page.locator("//*[contains(text(),'Register')]").click()
        page.locator("//*[@id='FirstName']").fill("Yogesh")
        page.locator("//*[@placeholder='Search store']").fill("Apple")
        AllAppleValues=page.locator("//*[@id='ui-id-1']").all_text_contents()
        for i in AllAppleValues:
            count=i.count()
            print(f'Count of all the Apple values:{count}')
            print(f' Apple Name :{i}')
        browser.close()
validate_title()
register()
