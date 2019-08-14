import pytest, os
from libraries.Environment import Env


@pytest.fixture(scope="module", autouse=True)
def env():
    yield Env(token='a7841dcb205d39e519e86d076f163bc6913dfe31')

@pytest.fixture(scope="module", autouse=True)
def just_print():
    print("我只是打印一段文本")