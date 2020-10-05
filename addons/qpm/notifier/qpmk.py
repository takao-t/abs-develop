#-*- coding:utf-8 -*-
# QPM用キー情報送信
# WebSocketでディスパッチャに投げるだけ
# websocket-clientが必要
# pip3 install websocket-client
#
# python3 qpmk.py 状態 キー番号-CID情報
#

import sys

from qpmnd_config import *

from websocket import create_connection

TARGET = 'ws://' + HOST + ':' + str(PORT)

try:
    sys.argv[2]
    cidname = sys.argv[2]
except:
    cidname = ""

try:
    sys.argv[1]

    s_message = sys.argv[1]

    ws = create_connection(TARGET)

    send_str = 'KEYINFO:' + TOKEN + ':' + s_message + ':' + cidname
    #print(send_str)

    ws.send(send_str)
    ws.close()

except:
    print("python3 qpmk.py STATUS KEYNUM-CIDINFO")
