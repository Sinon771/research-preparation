"""
元组创建后，不能替换、增加或删除其中的元素。
"""

box = (10, 20, 30, 40)
print(box[0])     # 读取 x
print(box[2:])    # 取出宽、高，结果仍是元组
print(len(box))   # 元素个数
# box[0] = 15     #TypeError: 'tuple' object does not support item assignment
"""
10
(30, 40)
4
"""

boxes = [
    (10, 20, 30, 40),
    (12, 21, 30, 40),
    (15, 23, 32, 40),
]
print(type(boxes))
print(type(boxes[0]))
print(boxes[2][2])
print(boxes[:2])
"""
<class 'list'>
<class 'tuple'>
32
[(10, 20, 30, 40), (12, 21, 30, 40)]
"""