x,y_true = 2.0,5.0
w,b=0.5,0.1
lr =0.01

y_hat = w*x+b
loss =(y_hat-y_true)**2
w_grad = 2*(y_hat-y_true)*x
b_grad = 2*(y_hat-y_true)

w_new=w-lr*w_grad
b_new=b-lr*b_grad

print(f"w_new:{w_new}, b_new:{b_new},loss:{loss},w_grad:{w_grad},b_grad:{b_grad}")

"""
output:
w_new:0.656, b_new:0.178,loss:15.209999999999999,w_grad:-15.6,b_grad:-7.8
"""