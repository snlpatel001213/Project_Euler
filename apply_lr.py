import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import math

torch.manual_seed(999)

if torch.cuda.is_available(): torch.cuda.manual_seed_all(999)


class data_generator:
    def make_positive(self,mask):
        mask[1,4] = 1
        mask[4,5] = 1
        mask[5,6] = 1
        mask[6,5] = 1
        mask[3,3] = 0
        mask[3,8] = 0
        mask[8,3] = 0
        mask[8,8] = 0
        return mask

    def make_negative(self, mask):
        mask[3, 3] = 1
        mask[3, 8] = 1
        mask[8, 3] = 1
        mask[8, 8] = 1
        mask[5, 4] = 0
        mask[4, 5] = 0
        mask[5, 6] = 0
        mask[6, 5] = 0
        return mask

    def generator(self, batch_size):
        data_batch = []
        data_label = []
        for i in range(batch_size):
            random_grid = np.random.random([10, 10])
            mask = random_grid
            data_batch.append(self.make_positive(mask).reshape(10*10))
            data_label.append([0,1])
            random_grid = np.random.random([10, 10])
            mask = random_grid
            data_batch.append(self.make_negative(mask).reshape(10*10))
            data_label.append([1,0])
        yield np.array(data_batch,dtype=np.float16), np.array(data_label,dtype=np.float16)

def accuracy_counter(predicted, target):
    predicted_max = predicted.argmax(dim=1)
    target_max    =  torch.Tensor(target).argmax(dim=1)
    return sum(predicted_max == target_max)/10.0



class simple_module_1(nn.Module):
    def __init__(self):
        super(simple_module_1, self).__init__()
        self.simple_linear = nn.Linear(100,2)

    def forward(self, input):
        return self.simple_linear(input)

def Train(model, data_generator_obj:data_generator,optimizer, epochs = 1000):
    optimizer.zero_grad()
    loss_tracker = []
    Accuracy_tracker = []
    for epoch in range(epochs):
        loss = 0
        for x,y in data_generator_obj.generator(5):
            y_ = model(torch.Tensor(x))
            Accuracy = accuracy_counter(y_, y)
            loss += objective(y_, torch.Tensor(y).float())
            loss_tracker.append(loss)
            Accuracy_tracker.append(Accuracy)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    return loss_tracker,Accuracy_tracker


simple_module = simple_module_1()
objective  = nn.MSELoss(reduce=True)
optimizer = optim.SGD(simple_module.parameters(),lr=0.01)
DG= data_generator()
loss_1,accuracy = Train(simple_module,DG,optimizer,epochs=200)


plt.plot(loss_1)
plt.plot(accuracy)
plt.show()