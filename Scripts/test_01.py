import pytest
import allure


class Test_01:


        def test_01(self):
            allure.step(title="第一个测试")
            with open('./phtot/text.png', 'rb') as f:
                allure.attach("sd", f, allure.attach_type.PNG)

            assert 0
