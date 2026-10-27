import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()# ① 必须第一行调用父类构造，否则参数注册机制不工作
        # ② 在这里"声明零件"：所有带参数的层都定义为成员变量
        self.conv1 = nn.Conv2d(1,16,kernel_size=3)
        self.conv2=nn.Conv2d(16,32,kernel_size=3)
        self.pool=nn.MaxPool2d(2)
        self.fc =nn.Linear(32*5*5,10) # ③ 全连接层的输入维度要算出来

    def forward(self,x):
        # ③ 在这里"组装流水线"：数据怎么流过零件
        x = self.pool(F.relu(self.conv1(x)))
        x= self.pool(F.relu(self.conv2(x)))
        x= x.view(x.size(0),-1) # ④ 展平为一维向量
        x= self.fc(x)
        return x

