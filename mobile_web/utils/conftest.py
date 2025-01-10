import pytest
from mobile_web.core.base import BasePage


@pytest.fixture
def mobile_emulation_driver(mobile_device_name):
    """
    Pytest fixture for mobile emulation WebDriver with parameterized device name.
    """
    page = None
    try:
        page = BasePage(mobile_device_name)
        yield page.driver
    finally:
        if page:
            page.driver.quit()

