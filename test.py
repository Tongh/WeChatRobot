# -*- coding: utf-8 -*-
#
# @Time    : 16/07/2018 15:18
#
# @Author  : WANG Wenxiao
#
# @FileName: test.py
#
from WeChat import WeChat


def main():
    app = WeChat()
    print(app.get_friend(userName="Sherryryryry"))


    app.logout()


if __name__ == "__main__":
    main()