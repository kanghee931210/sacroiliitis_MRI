"""####################### import requirement library ########################"""
from torch.autograd import Variable


def accuracy(output, target, topk=(1,)):

    # Computes the precision@k for the specified values of k
    maxk = max(topk)
    batch_size = target.size(0)
    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))
    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


def train_1epoch(_model, _train_loader, _optimizer, _loss_func, _epoch, _nb_epochs):
    print('==> Epoch:[{0}/{1}][training stage]'.format(_epoch, _nb_epochs))

    accuracy_list = []
    loss_list = []
    _model.train()
    for i, (data, label) in enumerate(_train_loader):

        label = label.cuda(async=True)
        input_var = Variable(data).cuda()
        target_var = Variable(label).cuda().long()

        output = _model(input_var)
        loss = _loss_func(output, target_var)
        loss_list.append(loss)

        # measure accuracy and record loss
        prec1 = accuracy(output.data, label, topk=(1, 5))
        accuracy_list.append(prec1)
        # print('Top1:', prec1)

        # compute gradient and do optimize step
        _optimizer.zero_grad()
        loss.backward()
        _optimizer.step()

    return float(sum(accuracy_list)/len(accuracy_list)), float(sum(loss_list)/len(loss_list)), _model


def test_1epoch(_model, _test_loader, _loss_func, _epoch, _nb_epochs):
    print('==> Epoch:[{0}/{1}][test stage]'.format(_epoch, _nb_epochs))

    accuracy_list = []
    loss_list = []
    _model.eval()
    for i, (data, label) in enumerate(_test_loader):
        label = label.cuda(async=True)
        input_var = Variable(data).cuda()
        target_var = Variable(label).cuda().long()

        output = _model(input_var)
        loss = _loss_func(output, target_var)
        loss_list.append(loss)

        # measure accuracy and record loss
        prec1 = accuracy(output.data, label, topk=(1, 5))
        accuracy_list.append(prec1)
        # print('Top1:', prec1)

    return float(sum(accuracy_list) / len(accuracy_list)), float(sum(loss_list) / len(loss_list)), _model

#  A  A
# (‘ㅅ‘=)
# J.M.Seo
