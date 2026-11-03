"""
需要实现以下三个接口：
接口	要求
box_area(box)	输入 (x, y, width, height)，通过赋值解包取得宽高，返回面积
is_valid_sample(sample, min_width=16, min_height=12)	目标可见，且宽高分别达到阈值时返回 True，否则返回 False
summarize_samples(samples, min_width=16, min_height=12)	调用前两个函数，返回统计字典

统计字典必须包含：
键	含义
"total_count"	输入样本总数
"valid_count"	有效样本数量
"total_area"	有效框面积之和
"mean_area"	有效框平均面积；没有有效样本时为 None

实现约束：
- 宽高达到阈值就算满足，使用 >=。
- 三个函数内部都不使用 print；外部接收返回值后打印。
- 不修改传入的列表、样本字典和框。
- 用循环累积，不使用 sum、列表推导式或第三方库。
- 统计函数调用有效性检查函数时，使用关键字传递两个阈值。
- 使用实际传入的参数，不能把阈值写死，也不能依赖外部固定名字的样本列表。
- 假设记录的键齐全、框中的值都是数字，暂不处理损坏数据。
"""
samples = [
    {"frame": "301.jpg", "box": (0, 0, 16, 12), "visible": True},
    {"frame": "302.jpg", "box": (2, 3, 20, 10), "visible": True},
    {"frame": "303.jpg", "box": (1, 1, 30, 20), "visible": False},
    {"frame": "304.jpg", "box": (4, 5, 18, 14), "visible": True},
    {"frame": "305.jpg", "box": (0, 0, 15, 20), "visible": True},
]
def box_area(box):
    _,_,w,h= box
    return w*h
def is_valid_sample(sample,min_width=16,min_height=12):
    if sample["visible"] and sample["box"][2]>=min_width and sample["box"][3]>=min_height:
        return True
    else:
        return False
def summarize_samples(samples, min_width=16, min_height=12):
    count={
        "total_count":0,
        "total_area":0,
        "valid_count":0,
        "mean_area":0,
    }
    for s in samples:
        count["total_count"]+=1
        if is_valid_sample(s,min_width=min_width,min_height=min_height):
            count["total_area"]+=box_area(s["box"])
            count["valid_count"]+=1
    if count["valid_count"]>0:
        count["mean_area"]=count["total_area"]/count["valid_count"]
    else:
        count["mean_area"]=None
    return count
parameter=(16,12)
c=summarize_samples(samples,*parameter)
if c["valid_count"]:
    print(f"total area:{c["total_area"]},valid count:{c["valid_count"]},total count:{c["total_count"]},mean area:{c["mean_area"]}")
else:
    print(f"no valid frame,mean area:{c['mean_area']}")