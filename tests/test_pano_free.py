from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://panorays.com/")
    page.get_by_role("link", name="Start Free Trial").click()
    page.get_by_placeholder("First Name*").click()
    page.get_by_placeholder("First Name*").fill("Test")
    page.get_by_placeholder("Last Name*").click()
    page.get_by_placeholder("Last Name*").fill("TestTest")
    page.get_by_placeholder("Company Email*").click()
    page.get_by_placeholder("Company Email*").fill("test@gmail.com")
    page.get_by_placeholder("Job Title*").click()
    page.get_by_placeholder("Job Title*").fill("PenTester")
    errormessage = page.get_by_text("Please enter your business email address.")
    expect(errormessage).to_be_hidden()
    page.get_by_role("button", name="Create Your Free Account").click()
    # print("No errors")
    # <div class="form-status"><div class="error">Please enter your business email address.</div></div>
    page.wait_for_timeout(1000)
    # errormessage = page.get_by_text("Please enter your business email address.")
    expect(errormessage).to_be_visible()
