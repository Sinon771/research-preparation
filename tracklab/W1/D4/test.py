"""
创建三个样本字典，键统一为 "frame"、"box"、"visible"：
变量名	文件名	框 (x, y, w, h)	可见性
sample_a	"021.jpg"	(5, 8, 16, 12)	True
sample_b	"022.jpg"	(8, 9, 30, 20)	False
sample_c	"023.jpg"	(9, 10, 15, 18)	True


要求：
1. 创建一个空列表 kept_samples。
2. 按“可见，且宽至少 16、高至少 12”筛选，将合格的整个样本加入其中。今天可以分别写三次判断，遍历放在 D5。
3. 打印筛选结果和保留数量。
4. 变化题：将规则改为“可见，且宽高都严格大于阈值”，重新筛选，避免混入上一轮结果。
"""
sample_a={
    "frame":"021.jpg",
    "box":(5,8,16,12),
    "visible":True,
}
sample_b={
    "frame":"022.jpg",
    "box":(8,9,30,30),
    "visible":False,
}
sample_c={
    "frame":"023.jpg",
    "box":(9,10,15,18),
    "visible":True,
}
kept_samples=[]
for i in sample_a,sample_b,sample_c:
    if i["visible"]==True and i["box"][2]>=16 and i["box"][3]>=12:
        kept_samples.append(i)
print(f"list={kept_samples},length={len(kept_samples)}")
"""
list=[{'frame': '021.jpg', 'box': (5, 8, 16, 12), 'visible': True}],length=1

初始时两个错误点：
1.range(sample_a,sample_b,sample_c)是错的
2.i["box"[2]]是错的，i["box"][2]是对的
"""
