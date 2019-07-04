import random
import time

import win32con
import win32gui

# hwnd = win32gui.FindWindow(None, "无标题 - 画图")
hwnd = win32gui.FindWindow(None, "GEOVIA Surpac 6.9 - C:/Users/linpe (Profile:)")

# 隐含窗口标题栏
ISTYLE = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 100, 10, 640, 480, win32con.SWP_SHOWWINDOW)
win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, ISTYLE & win32con.GW_CHILD & win32con.WS_CAPTION)

# 参数1：控制的窗体
# 参数2：大致方位，HWND_TOPMOST上方
# 参数3：位置x
# 参数4：位置y
# 参数5：长度
# 参数6：宽度
# while True:
#     time.sleep(0.2)
#     x = random.randrange(600)
#     y = random.randrange(800)
#     win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, 640, 480, win32con.SWP_SHOWWINDOW)
