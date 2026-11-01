"""
本题约定：每个样本都包含这些键，框内都是数字，暂时不处理缺键、字符串或损坏记录。

有效条件沿用 D4：可见，并且宽至少为 16、高至少为 12。

要求：
1. 使用 enumerate 遍历，编号从 1 开始。
2. 对每个有效样本，打印其原始编号、文件名和框面积。
3. 遍历结束后，打印输入样本总数、有效帧数、有效框总面积和平均框面积。
4. 没有有效帧时，数量和总面积输出 0，平均面积位置输出“无有效帧”。
5. 用循环亲手完成累加，本题暂不使用 sum、列表推导式或第三方库。
"""

samples = [
    {"frame": "101.jpg", "box": (5, 8, 16, 12), "visible": True},
    {"frame": "102.jpg", "box": (8, 9, 30, 20), "visible": False},
    {"frame": "103.jpg", "box": (2, 3, 20, 15), "visible": True},
    {"frame": "104.jpg", "box": (4, 6, 0, 12), "visible": True},
    {"frame": "105.jpg", "box": (7, 1, 18, 12), "visible": True},
    {"frame": "106.jpg", "box": (9, 2, 15, 18), "visible": True},
]

flag=0
total=0
vaild=0
for i,sample in enumerate(samples,start=1):
    if sample["visible"] and sample["box"][2]>=16 and sample["box"][3]>=12:
        area=sample["box"][2]*sample["box"][3]
        total+=area
        vaild+=1
        print(f"index:{i},name:{sample["frame"]},area:{area}")
        flag=1
if flag:
    print(f"总数:{len(samples)},total area:{total},vaild frames number:{vaild},average:{total/vaild}")
else:
    print("no vaild frame,total area:0,vaild frames number:0")

"""
index:1,name:101.jpg,area:192
index:3,name:103.jpg,area:300
index:5,name:105.jpg,area:216
总数:6,total area:708,vaild frames number:3,average:236.0
"""
