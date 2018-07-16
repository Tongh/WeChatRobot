# -*- coding: utf-8 -*-
#
# @Time    : 16/07/2018 16:06
#
# @Author  : WANG Wenxiao
#
# @FileName: WeChat.py
#
import itchat as wechat
import time
import functools


def log(status=True, text="execute"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if status:
                print('%s %s():' % (text, func.__name__))
            func(*args, **kw)
            if status:
                print("\t [Succes]")
        return wrapper
    return decorator


class WeChat:
    _ME = 'filehelper'
    _debug_mod = True

    def __init__(self, debug_mod=True):
        self._debug_mod = debug_mod
        self.run()

    @log(_debug_mod)
    def run(self):
        def lc():
            print("login succes")
        def ec():
            print("logout!")
        wechat.auto_login(enableCmdQR=-2, hotReload=True, loginCallback=lc, exitCallback=ec)

    @log(_debug_mod)
    def logout(self):
        time.sleep(3)
        wechat.logout()

    @log(_debug_mod)
    def _make_message(self, msg):
        return "[%s] : %s" % (time.ctime(), msg)

    @log(_debug_mod)
    def send_test(self, msg="Can u receive me?中文可以接受吗？", target=_ME):
        wechat.send(self._make_message(msg), toUserName=target)

    @log(_debug_mod)
    def get_friend(self, **kw):
        return wechat.search_friends(**kw)


