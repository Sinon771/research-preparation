"""
要求如下：
- parse_box：每行恰好五个字段；图片名去掉首尾空白后不能为空；四个坐标字段转换为 float。
- 本题允许 x、`y` 为负数，但宽和高必须大于零。
- 空白行视为格式错误，不跳过。切分后的图片名也可以单独调用 .strip()。
- load_boxes：使用 with 逐行读取，返回记录列表。
- 解析失败时抛出 ValueError，信息包含文件路径、标注行号、该行原文，并保留原始异常作为原因。
- 文件不存在时，让原来的 FileNotFoundError 正常暴露；不要把它伪装成标注格式错误。
"""
from pathlib import Path

root=Path("D:/Project/Engineering_Competency_Development/research-preparation/tracklab/W2/D5")
file=root/"test.txt"

def parse_box(raw):
    fields = raw.strip().split(",")

    # 先检查数量，再通过索引读取字段。
    if len(fields) != 5:
        raise ValueError(
            f"每行必须有 5 个字段，实际有 {len(fields)} 个"
        )

    # 整行 strip() 不会去掉图片名与逗号之间的空格，
    # 所以图片名字段还要单独处理。
    frame = fields[0].strip()

    if frame == "":
        raise ValueError("图片名不能为空")

    # 无法转换时，float() 自己会抛出 ValueError。
    x = float(fields[1])
    y = float(fields[2])
    w = float(fields[3])
    h = float(fields[4])

    if w <= 0 or h <= 0:
        raise ValueError(
            f"宽和高必须大于 0，实际为 w={w}, h={h}"
        )

    return {
        "frame": frame,
        "box": [x, y, w, h],
    }


def load_boxes(path):
    path = Path(path)
    records = []

    with open(path, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            try:
                record = parse_box(raw)
            except ValueError as exc:
                message = (
                    f"{path} 第 {line_no} 行标注无效；"
                    f"原文：{repr(raw)}；原因：{exc}"
                )
                raise ValueError(message) from exc

            records.append(record)

    return records

lst=load_boxes(file)
print(lst)