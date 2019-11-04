# -*- coding:utf-8 -*-
from ucumos.wrapped import load_packaged_model
from PIL import Image
import base64
import io

model = load_packaged_model('./out/场景识别')  # 从模型文件夹加载模型对象
model.init_model_data.inner('')  # 初始化模型数据


def read_image(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
        input_buffer = io.BytesIO()
        image.save(input_buffer, format='JPEG')
        return str(base64.b64encode(input_buffer.getvalue()), encoding='utf-8')
    except Exception as e:
        print(400, "The provided input is not a valid image (PNG or JPG required).")

image_path = 'test_files/bakery.jpg'
img_base64 = read_image( image_path)
print( img_base64)
result = model.classify.inner(img_base64)
print(result)