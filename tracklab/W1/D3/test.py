"""
按顺序完成以下操作：
1. 创建 frames 和 boxes，分别保存帧名与框。
2. 打印最后一帧的文件名，以及它对应框的宽度。
3. 发现第二条框记录有误：先用 old_box 保留旧框，再把第二条记录整体替换为 (44, 52, 20, 10)。打印旧框和更正后的框。
4. 在两个列表末尾追加一条对应记录："021.jpg"，框为 (54, 56, 24, 12)。
5. 用切片分别取出第 2 至第 4 帧的帧名和框，保存到两个新变量，再打印。这里的“第几帧”按列表顺序计数。
6. 打印两个完整列表各自的长度，确认追加操作后的数量一致。
"""

frames=["010.jpg","012.jpg","015.jpg","018.jpg"]
tuple_=[(40,50,20,10),(43,51,20,10),(47,53,22,10),(50,54,22,12)]
print(f"lastest frame:{frames[-1]},width:{tuple_[-1][2]}")

old_box=tuple_[1]
tuple_[1]=(44,52,20,10)
print(f"old box:{old_box},new box:{tuple_[1]}")


frames.append("021.jpg")
"""
旧版tuple_增加框：tuple_=[(40,50,20,10),(43,51,20,10),(47,53,22,10),(50,54,22,12),(54,56,24,12)]
其实tuple_是list，里面的元素才是元组，所以直接tuple_.append()就行了
"""
tuple_.append((54,56,24,12))
f2_4=frames[1:4]
t2_4=tuple_[1:4]
print(f"f={f2_4},t={t2_4}")

print(f"frames list={frames},tuple list={tuple_},len f{len(frames)},len t={len(tuple_)}")

"""
lastest frame:018.jpg,width:22
old box:(43, 51, 20, 10),new box:(44, 52, 20, 10)
f=['012.jpg', '015.jpg', '018.jpg'],t=[(44, 52, 20, 10), (47, 53, 22, 10), (50, 54, 22, 12)]
frames list=['010.jpg', '012.jpg', '015.jpg', '018.jpg', '021.jpg'],tuple list=[(40, 50, 20, 10), (44, 52, 20, 10), (47, 53, 22, 10), (50, 54, 22, 12), (54, 56, 24, 12)],len f5,len t=5
"""

print((10),type((10)),(10,),type((10,)))#10 <class 'int'> (10,) <class 'tuple'>
# print(tuple(10),type(tuple(10)),tuple(10,),type(tuple(10,)))#四个全报错，不允许这样写
