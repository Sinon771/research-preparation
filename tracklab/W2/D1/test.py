"""
实现下面三个接口，不需要写默认参数：
接口	                                                        职责与返回结果
box_area(box)	                                        输入 (x, y, width, height)，返回面积
is_valid_sample(sample, min_width, min_height)	        同时满足可见、宽高达到阈值时返回 True，否则返回 False
summarize_samples(samples, min_width, min_height)	    返回包含统计结果的字典

统计字典统一包含：
键	                含义
"total_count"	输入样本总数
"valid_count"	有效样本数量
"total_area"	有效框面积之和
"mean_area"	    有效框平均面积；没有有效样本时为 None

要求：
- 统计函数实际调用前两个函数，复用它们的逻辑。
- 三个函数内部都不使用 print，由外部接收结果后打印。
- 用循环累加，不用 sum、列表推导式或第三方库。
- 函数使用传入的参数，不依赖外部某个固定名字的样本列表。
- 不修改输入样本。
- 暂时假设每条记录的键齐全，框中的值都是数字。
使用这批数据：
samples = [
    {"frame": "201.jpg", "box": (0, 0, 20, 12), "visible": True},
    {"frame": "202.jpg", "box": (3, 4, 16, 15), "visible": True},
    {"frame": "203.jpg", "box": (1, 2, 40, 20), "visible": False},
    {"frame": "204.jpg", "box": (5, 6, 15, 20), "visible": True},
    {"frame": "205.jpg", "box": (7, 8, 30, 11), "visible": True},
]
完成三种运行检查：
1. 普通情况：最小宽 16、最小高 12。预期总数 5、有效数 2、总面积 480、平均面积 240.0。
2. 无有效样本：最小宽和最小高都设为 1000。数量与面积为 0，平均面积为 None。
3. 空列表：样本总数也应为 0，其余遵循无有效样本的约定。
"""
samples = [
    {"frame": "201.jpg", "box": (0, 0, 20, 12), "visible": True},
    {"frame": "202.jpg", "box": (3, 4, 16, 15), "visible": True},
    {"frame": "203.jpg", "box": (1, 2, 40, 20), "visible": False},
    {"frame": "204.jpg", "box": (5, 6, 15, 20), "visible": True},
    {"frame": "205.jpg", "box": (7, 8, 30, 11), "visible": True},
]

def box_area(box):
    return box[2]*box[3]
def is_valid_sample(sample,min_width,min_height):
    if sample["visible"] and sample["box"][2]>=min_width and sample["box"][3]>=min_height:
        return True
    else:
        return False
def summarize_samples(samples, min_width, min_height):
    count={
        "total_count":0,
        "total_area":0,
        "valid_count":0,
        "mean_area":0,
    }
    for s in samples:
        count["total_count"]+=1
        if is_valid_sample(s,min_width,min_height):
            count["total_area"]+=box_area(s["box"])
            count["valid_count"]+=1
    if count["valid_count"]>0:
        count["mean_area"]=count["total_area"]/count["valid_count"]
    return count
c=summarize_samples(samples,16,12)
if c["valid_count"]:
    print(f"total area:{c["total_area"]},valid count:{c["valid_count"]},total count:{c["total_count"]},mean area:{c["mean_area"]}")
else:
    print(f"no valid frame,mean area:None")

"""
total area:480,valid count:2,total count:5,mean area:240.0
"""