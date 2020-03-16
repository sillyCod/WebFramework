# -*- coding: utf-8 -*-
# time: 2019/4/10 下午2:06
from app import create_app
from config import app_conf


app = create_app(app_conf)

if __name__ == '__main__':
    app.run(port=6666)
