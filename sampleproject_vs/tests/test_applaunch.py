from playwright.sync_api import Page, expect


def test_launch_navigate_url(page: Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    url = page.url
    print("Url of the App: " + url)
    title = page.title()
    print("Title of the App:" + title)