"""
@Author : ansq
@File   : test_core.py
@Date   : 2021/4/12
@Desc   :
"""


def test_version():
    from ddmc_apitest import __version__
    assert isinstance(__version__, str)