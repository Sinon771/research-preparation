frames = ["031.jpg", "034.jpg", "040.jpg"]

for frame in frames:
    print(frame)

for i in range(len(frames)):
    print(i,frames[i])

#range(起始，终止，步长)，左闭右开
for i in range(0,len(frames),2):
    print(i,frames[i])

#enumerate：遍历时，同时取得编号和元素
for index,frame in enumerate(frames):
    print(index,frame)

for index,frame in enumerate(frames,start=5):
    print(index,frame)

