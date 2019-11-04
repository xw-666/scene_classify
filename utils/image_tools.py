# -*- coding: utf-8 -*-
import io
import base64
from PIL import Image, ExifTags


def read_img_from_base64(img_base64):
    image = Image.open(io.BytesIO(base64.b64decode(img_base64.encode())))

    # 自动按拍摄时相机的重心旋转图像
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
    except:
        pass

    return image


def get_base64_from_file(path):
    with open(path, 'rb') as file:
        return str(base64.b64encode(file.read()), encoding='utf-8')
