import json

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from test.utils import Utils
import os
from datetime import datetime
from config.config_helper import web_url
import pyscreenrec



def pytest_addoption(parser):
    parser.addoption(
        "--user_role",
        action="store",
        default="admin",
        help="Specify the user role for login (e.g., admin)"
    )


@pytest.fixture(scope="function")
def setup(request):
    global driver
    record_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "recording")
    if not os.path.exists(record_dir):
        os.makedirs(record_dir)
    output_filename = os.path.join(record_dir, f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")
    recorder = pyscreenrec.ScreenRecorder()
    recorder.start_recording(output_filename,30, {
	"mon": 1,
	"left": 100,
	"top": 100,
	"width": 1920,
	"height": 1080
})
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})
    # options.add_argument("--headless")
    # options.add_argument("--disable-notifications")
    # options.add_argument("--incognito")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")  # Disable GPU for headless mode
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    driver.get(web_url.get("url"))
    user_role = request.config.getoption("--user_role")
    login_page = LoginPage(driver)
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config", "data.json")
    with open(config_path, 'r') as file:
        data = json.load(file)
        print(data)
    if user_role == "admin":
        login_page.login(data["admin"]["username"], data["admin"]["password"])
    else:
        login_page.login("User", "user123")
    assert login_page.validate_successful_login(), "Login was not successful."
    Utils.get_logger().info("Login successful, navigating to recruitment page.")
    request.cls.driver = driver
    request.cls.login_page = login_page
    yield driver  # Run all other pytest_runtest_makereport non wrapped hooks
    driver.quit()
    recorder.stop_recording()
    Utils.get_logger().info(f"Recording saved at: {output_filename}")


def take_screenshot(driver, test_name):
    """Captures a screenshot and saves it in the 'screenshot' folder."""
    screenshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "screenshot")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to take a screenshot if a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            test_name = item.name
            screenshot_path = take_screenshot(driver, test_name)
            print(f"Screenshot saved at: {screenshot_path}")





# def record_test_execution():
#     # Initialize screen recorder
#     record_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recordings")
#     if not os.path.exists(record_dir):
#         os.makedirs(record_dir)
#     output_filename = os.path.join(record_dir, f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")
#     recorder = pyscreenrec.ScreenRecorder(output=output_filename)
#     return recorder