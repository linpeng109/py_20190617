import qrcode

# 二维码内容
data = "整个系统中，数据的读出和写入是处理的第一步，各" \
       "企业中原有系统的复杂性，决定了与原有系统的对接不" \
       "可能采用统一的方式，为此，在数据集成系统中，归纳了" \
       "一下几种方式，需要根据实际情况，优化选择"
# 生成二维码
img = qrcode.make(data=data)
# 直接显示二维码
img.show()
# 保存二维码为文件
img.save("D:/Workspace/OpencvVideo/baidu.png")
