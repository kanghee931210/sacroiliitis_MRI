"""####################### import requirement library ########################"""

import torchvision.models as models


def set_model(model_name, pretrained):
    if model_name == 'resnet18':
        select_model = models.resnet18(pretrained=pretrained)
    elif model_name == 'resnet34':
        select_model = models.resnet34(pretrained=pretrained)
    elif model_name == 'resnet50':
        select_model = models.resnet50(pretrained=pretrained)
    elif model_name == 'resnet101':
        select_model = models.resnet101(pretrained=pretrained)
    elif model_name == 'resnet152':
        select_model = models.resnet152(pretrained=pretrained)
    else:
        raise ValueError

    return select_model

#  A  A
# (‘ㅅ‘=)
# J.M.Seo
