# 场景分类器

此模型可识别Places2数据集的Places365-Standard子集中的365种不同类别的场景/位置。 该模型基于Places365-CNN模型，由使用ResNet架构的预训练深度卷积网络组成，并在ImageNet-2012数据集上进行训练。 然后，在Places365-Standard数据集上微调预训练的模型。 该模型的输入是224x224的图像，输出是估计的类别概率的列表。

## 参考文献

* _B. Zhou, A. Lapedriza, A. Khosla, A. Oliva, and A. Torralba_, ["Places: A 10 million Image Database for Scene Recognition"](http://places2.csail.mit.edu/PAMI_places.pdf), IEEE Transactions on Pattern Analysis and Machine Intelligence, 2017.

* _B. Zhou, A. Lapedriza, J. Xiao, A. Torralba and A. Oliva_, ["Learning Deep Features for Scene Recognition
using Places Database"](http://places.csail.mit.edu/places_NIPS14.pdf), Advances in Neural Information Processing Systems 27, 2014.

* _K. He, X. Zhang, S. Ren and J. Sun_, ["Deep Residual Learning for Image Recognition"](https://arxiv.org/pdf/1512.03385), CoRR (abs/1512.03385), 2015.

* [Places2 Project Page](http://places2.csail.mit.edu/)

* [Places365-CNN GitHub Page](https://github.com/CSAILVision/places365)

## API接口

该模型实现了1个API接口，其调用形式和返回值格式如下：

- predict：场景分类模型，输入base64编码图片，返回目标场景和估计正确率。

    - HTTP方法：POST

    - 模型方法：classify

    - HTTP请求体格式：{“image”：<压缩图像的base64编码字符串>}

    - HTTP响应体格式：{“value”: <JSON列表字符串>}
    
    其中JSON列表字符串字符串中JSON对象的格式如下：
     
        [
            [<中文名1>, <英文名1>, <信心度1>], 
            [<中文名2>, <英文名2>, <信心度2>], 
            [<中文名3>, <英文名3>, <信心度3>], 
        ]
         
## 模型托管和演示

### 模型打包及导入

1. 运行model_pack.py，将在out文件夹下生成一个压缩文件：场景识别.zip。

2. 进入CubeAI平台“模型导入”界面（[https://cubeai.dimpt.com/#/ucumos/onboarding](https://cubeai.dimpt.com/#/ucumos/onboarding)），将上述生产的zip文件导入CubeAI平台。

### 模型托管

- https://cubeai.dimpt.com/#/ucumos/solution/6e399ab9d3c940e7a77521e243eff7f2/view
    
### 模型能力开放

- https://cubeai.dimpt.com/#/ai-ability/ability/bd54000128954220a4076a1a700650f4/view
    
### 模型演示

- https://cubeai.dimpt.com/udemo/#/scene-classify
