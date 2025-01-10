from mobile_web.core.base import BasePage
from mobile_web.page.index import Index
from mobile_web.page.browse import Browse
from mobile_web.page.streamer_personal import StreamerPersonal


class TestWeb:
    def setup_method(self):
        self.driver = BasePage("Nexus 5")  # 這是你的共用資源

    def teardown_method(self):
        self.driver.quit()

    def test_wap(self):

        # Given
        index_page = Index(self.driver)
        browse_page = Browse(self.driver)
        streamer_personal_page = StreamerPersonal(self.driver)

        # When
        index_page.go_to_index_page()
        index_page.go_to_browse_page()
        browse_page.sent_wording_to_search('StarCraft II')
        browse_page.scroll_down_2_times()
        browse_page.selected_streamer()

        # Then
        streamer_personal_page.screenshot_personal_page()



