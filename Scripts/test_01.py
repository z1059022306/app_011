import pytest
import allure
import pytest, sys, os,time
sys.path.append(os.getcwd())
from Page.login_page import Login_Page
from Page.setting_page import Setting_Page
from Page.Page import Page
from Base.init_driver import get_driver
from Base.read_data import Op_Data
import allure



class Test_01:

    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(get_driver())

    def teardown_class(self):
        self.page_obj.driver.quit()

    def get_ph(self):
        img_name = './phtot/%d.png' % int(time.time())
        self.page_obj.driver.get_sereenshot_as_file(img_name)
        with open(img_name, 'rb') as f:
            allure.attach("sd", f.read(), allure.attach_type.PNG)

    def test_01(self):

        self.page_obj.get_login_page().click_my_btn()
        assert 0, self.get_ph()

    def test_02(self):
        assert 0,self.get_ph()
