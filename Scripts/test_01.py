import pytest
import allure


class Test_01:

    def get_ph(self):
        with open('./phtot/text.png', 'rb') as f:
            allure.attach("sd", f.read(), allure.attach_type.PNG)
    def test_01(self):
        allure.step(title="第一个测试")


        assert 0,self.get_ph()
