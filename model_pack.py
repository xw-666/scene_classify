# -*- coding: utf-8 -*-
from ucumos.modeling import Model
from ucumos.session import AcumosSession
from ucumos.metadata import Requirements
from model_service import ModelService

scene_classifier = ModelService()

# 封装模型API接口函数： 初始化模型数据。该接口函数仅供系统调用，必须存在，不要修改或删除！！！
def init_model_data(text: str) -> str:
    scene_classifier.init_model_data()
    return 'model_data_loaded'

def classify(image: str) -> str:
    '''
    输入图片，返回标签标识符,类标签,类别标签的预测概率
    '''
    return scene_classifier.classify(image)


model = Model(init_model_data=init_model_data, classify=classify)
session = AcumosSession()
req = Requirements(reqs=['torch==0.3.1', 'torchvision==0.2.1', 'PIL'], req_map={'PIL': 'pillow'}, scripts=['./model_service.py'], packages=['./core'])
session.dump(model, '场景识别', './out/', req)