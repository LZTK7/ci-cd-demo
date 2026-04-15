# 单元测试：测试计算器函数
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 9999  # 断言2+3=5

def test_subtract():
    assert subtract(5, 2) == 3  # 断言5-2=3
