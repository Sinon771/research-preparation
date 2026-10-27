import torch
import torchvision
import matplotlib.pyplot as plt

ds =torchvision.datasets.MNIST(root='W1/D2',train=True,download=True,transform=torchvision.transforms.ToTensor())

img,label=ds[0]

print("len=" + str(len(ds)) + ", img.shape=" + str(img.shape) + ", label=" + str(label))

loader =torch.utils.data.DataLoader(ds,batch_size=64,shuffle=True)
x,y = next(iter(loader))
print("x.dtype=" + str(x.dtype) + ", x.shape=" + str(x.shape) + ", y.shape=" + str(y.shape))
plt.imshow(x[0][0],cmap='gray')
plt.title(f"label = {y[0].item()}")   # 顺便把这批第0张的标签写在标题上
plt.show()                             # ← 缺的就是这行