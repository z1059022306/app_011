import pytest
import allure


class Test_01:

    with open('./phtot/text.png','rb') as f:
        @allure.attach("sd",f,allure.attach_type.PNG)
        @allure.step(title="第一个测试")
        def test_01(self):
            assert 0
