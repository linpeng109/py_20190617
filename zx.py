# 'utf-8'
import logging
import os
import random

import zxing
from PIL import Image

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(level=logging.INFO)

DEBUG = (logging.getLevelName(logger.getEffectiveLevel()) == 'DEBUG')


def ocr_qrcode_zxing(filename):
    img = Image.open(filename)
    ran = int(random.random() * 100000)
    img.save('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))
    zx = zxing.BarCodeReader()
    data = ''

    zxdata = zx.decode('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))

    os.remove('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))

    if zxdata:
        logger.debug(u'zxing识别二维码:%s,内容: %s' % (filename, zxdata))
        data = zxdata
    else:
        logger.error(u'识别zxing二维码出错:%s' % (filename))
        img.save('%s-zxing.jpg' % filename)
    return data


if __name__ == '__main__':
    filename = r'D:/Workspace/OpencvVideo/baidu.png'
    ltext = ocr_qrcode_zxing(filename)
    logger.info(u'[%s]Zxing二维码识别:[%s]!!!' % (filename, ltext))

print(ltext)
