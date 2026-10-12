import torch

x=torch.tensor(2.0)
y_true=torch.tensor(5.0)
w=torch.tensor(0.5,requires_grad=True)
b=torch.tensor(0.1,requires_grad=True)

y_hat=w*x+b
loss=(y_hat-y_true)**2
loss.backward()
print(f"loss:{loss.item()},w_grad:{w.grad.item()},b_grad:{b.grad.item()}")

"""
output:
loss:15.209999084472656,w_grad:-15.600000381469727,b_grad:-7.800000190734863
"""
