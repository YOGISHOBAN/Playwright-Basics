from playwright.sync_api import sync_playwright,expect
def browserlaunch() :
    p=sync_playwright().start()
    browser=p.chromium.launch(channel="chrome",headless=False)
    page=browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    return p,page,browser
def test_singledropdownselect():
    print(f'Case 1 Running')
    p,page,browser=browserlaunch()
    page.wait_for_timeout(5000)
    page.locator("#country").select_option("India")
    page.screenshot(path="CountrySelect.jpg",full_page=True)
    browser.close()
    p.stop()
def test_multiselectdropdown():
    print(f'Case 2 Running')
    p,page,browser=browserlaunch()
    page.wait_for_timeout(5000)
    Values=["Blue","Yellow","Red"]
    dropdownvalues=page.locator("#colors").all_text_contents()
    page.locator("#colors").select_option(Values)
    expect(page.locator("//*[@id='colors']")).to_be_visible()
    page.screenshot(path="MultipleSelect.jpg",full_page=True)
    print(f'Number of Colours count{len(dropdownvalues)}')
    browser.close()
    p.stop()
if __name__ == '__main__':
    test_singledropdownselect()
    test_multiselectdropdown()