import torch
from torch.autograd import Variable as V
from torchvision import transforms as trn
from torch.nn import functional as F
import base64
from utils import image_tools
import io
from PIL import Image
import json


class ModelCore(object):
    def __init__(self):
        model_path = 'core/model_data/whole_resnet18_places365_python36.pth'
        self.model = torch.load(model_path, map_location=lambda storage, loc: storage)  # cpu only for now ...
        file_name = 'core/model_data/cn_categories_places365.txt'
        classes = list()
        with open(file_name) as class_file:
            for line in class_file:
                classes.append(line.strip().split(' ')[0][3:])
        self.classes = tuple(classes)

    def preprocess_image(self, img_base64, target):
        # load the image transformer
        image = image_tools.read_img_from_base64(img_base64)
        centre_crop = trn.Compose([
            trn.Resize(target),
            trn.CenterCrop(224),
            trn.ToTensor(),
            trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        return V(centre_crop(image).unsqueeze(0), volatile=True)

    def post_process_result(self, probs, idxs, classes, topk=5):
        results = []
        for i in range(0, topk):
            result = (idxs[i], classes[idxs[i]], probs[i])
            results.append(result)
        return results

    def _pre_process(self, x):
        return self.preprocess_image(x, (256,256))

    def _post_process(self, x):
        probs, idx = x.sort(0, True)
        return self.post_process_result(probs, idx, self.classes)

    def _predict(self, x):
        logit = self.model.forward(x)
        probs = F.softmax(logit, 1).data.squeeze()
        return probs

    def classify(self, x):
        pre_x = self._pre_process(x)
        prediction = self._predict(pre_x)
        result = self._post_process(prediction)
        re_list = []
        for item in result:
            if len(item) > 0:
                temp = []
                temp.append(item[1])
                temp.append(item[2])
                re_list.append(temp)
        return json.dumps(re_list, ensure_ascii=False)
