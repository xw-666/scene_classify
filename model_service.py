# -*- coding: utf-8 -*-
import os
from core.model_core import ModelCore
from PIL import Image
import base64
import io



class ModelService(object):

    # 声明model_core对象并赋空置。必须存在，不要修改或删除！！！
    def __init__(self):
        self.model_core = None

    # 从文件中加载模型数据，例如预训练好的模型参数等。必须存在，不要修改或删除！！！
    def init_model_data(self):
        if self.model_core is None:
            cwd = os.getcwd()
            if cwd == '/app':  # 在docker容器中运行
                os.chdir('/app/model/model/scripts/user_provided')

            try:
                self.model_core = ModelCore()
            except:
                self.model_core = None

            os.chdir(cwd)

    # 模型接口函数
    def classify(self, img_base64):
        return self.model_core.classify(img_base64)


if __name__ == "__main__":

    def read_image(image_path):
        try:
            image = Image.open(image_path).convert('RGB')
            input_buffer = io.BytesIO()
            image.save(input_buffer, format='JPEG')
            return str(base64.b64encode(input_buffer.getvalue()), encoding='utf-8')
        except Exception as e:
            print(400, "The provided input is not a valid image (PNG or JPG required).")

    scene_classifier = ModelService()
    scene_classifier.init_model_data()
    image_path = 'test_files/bakery.jpg'
    img_base64 = read_image( image_path)
    print( img_base64)
    preds = scene_classifier.classify(img_base64)
    print( preds)