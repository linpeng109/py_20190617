import qrcode

# 二维码内容
data = "http://2680403ep2.wicp.vip:34454/#/"
# 生成二维码
img = qrcode.make(data=data)
# 直接显示二维码
img.show()
# 保存二维码为文件
img.save("D:/Workspace/OpencvVideo/sinomine.png")
