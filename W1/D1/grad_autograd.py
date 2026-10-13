import torch

x=torch.tensor(2.0)
y_true=torch.tensor(5.0)
w=torch.tensor(0.5,requires_grad=True)
b=torch.tensor(0.1,requires_grad=True)

lr=0.01

y_hat=w*x+b
loss=((y_hat-y_true)**2).mean()
loss.backward()
print(f"loss:{loss.item()},w_grad:{w.grad.item()},b_grad:{b.grad.item()}")

"""
output:
loss:15.209999084472656,w_grad:-15.600000381469727,b_grad:-7.800000190734863
"""
for step in range(200):
    y_hat=w*x+b
    loss=(y_hat-y_true)**2
    loss.backward()

    #更新参数
    with torch.no_grad():
        w-=lr*w.grad
        b-=lr*b.grad

    #梯度清零
    w.grad.zero_()
    b.grad.zero_()

    if step % 20 == 0 or step==199:
        print(f"step:{step}, w:{w.item()}, b:{b.item()}, loss:{loss.item()}, w_grad:{w.grad.item()}, b_grad:{b.grad.item()}")

"""
output:
loss:15.210000991821289,w_grad:-15.600000381469727,b_grad:-7.800000190734863
step:0, w:0.812000036239624, b:0.25600001215934753, loss:15.210000991821289, w_grad:0.0, b_grad:0.0
step:20, w:1.908272385597229, b:0.8041360974311829, loss:0.17763307690620422, w_grad:0.0, b_grad:0.0
step:40, w:2.0415537357330322, b:0.8707765340805054, loss:0.002625534310936928, w_grad:0.0, b_grad:0.0
step:60, w:2.0577573776245117, b:0.8788784146308899, loss:3.881137308781035e-05, w_grad:0.0, b_grad:0.0
step:80, w:2.059727430343628, b:0.8798633217811584, loss:5.741005679738009e-07, w_grad:0.0, b_grad:0.0
step:100, w:2.059967041015625, b:0.8799830675125122, loss:8.557435648981482e-09, w_grad:0.0, b_grad:0.0
step:120, w:2.0599958896636963, b:0.8799977898597717, loss:1.3096723705530167e-10, w_grad:0.0, b_grad:0.0
step:140, w:2.0599989891052246, b:0.8799997568130493, loss:5.6843418860808015e-12, w_grad:0.0, b_grad:0.0
step:160, w:2.0599989891052246, b:0.8800004124641418, loss:2.0463630789890885e-12, w_grad:0.0, b_grad:0.0
step:180, w:2.0599989891052246, b:0.8800004124641418, loss:2.0463630789890885e-12, w_grad:0.0, b_grad:0.0
step:199, w:2.0599989891052246, b:0.8800004124641418, loss:2.0463630789890885e-12, w_grad:0.0, b_grad:0.0
"""