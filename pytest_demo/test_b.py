import pytest



def test_1(login):
    print("测试用例1111")
    assert 1==1


def test_2(login):
    print("测试用例22222")
    assert 1==1


@pytest.mark.repeat(3)
def test_3(login):
    print("测试用例3333")


def test_4(login):
    print("测试用例44444444")
    assert 1==1
