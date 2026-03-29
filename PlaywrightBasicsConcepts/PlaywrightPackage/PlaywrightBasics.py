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
def Login():
    with sync_playwright() as p:
        browser=p.chromium.launch(channel="chrome",headless=False)
        page=browser.new_page()
        page.goto("https://www.demoblaze.com/")
        page.wait_for_timeout(5000)
        page.locator("//a[contains(text(),'Log in')]").click()
        page.locator("//*[@id='loginusername']").fill("username")
        page.locator("//*[@id='loginpassword']").fill("password")
        page.locator("//button[contains(text(),'Log in')]").click()
        page.wait_for_timeout(8000)
        page.locator("//*[contains(text(),'Monitors')]").click()
        page.wait_for_timeout(8000)
        AllMonitorValues=page.locator("//*[@id='tbodyid']//following::a[@class='hrefch']").all_text_contents()
        print(f'Count of all the Monitor values:{len(AllMonitorValues)}')
        for i in AllMonitorValues:
            print(f' Monitors Name :{i}')
        page.screenshot(path="MonitorSnap.png",full_page=True)
        browser.close()
validate_title()
Login()
