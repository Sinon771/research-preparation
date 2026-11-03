from pathlib import Path


def parse_width(raw):
    fields = raw.strip().split(",")
    width = float(fields[1])
    return {"frame": fields[0], "width": width}


def read_widths(path):
    records = []

    with open(path, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            print("正在读取：", line_no, repr(raw))
            try:
                record = parse_width(raw)
            except ValueError as exc:
                message=f"{path}第{line_no}行无法解析，原文:{repr(raw)}"
                raise ValueError(message) from exc
            
            records.append(record)
    return records


p = Path("D:/Project/Engineering_Competency_Development/research-preparation/tracklab/W2/D5/width_demo.txt")
result = read_widths(p)
print(result)

"""
正在读取： 1 'demo_a.jpg,12.5\n'
正在读取： 2 'demo_b.jpg,bad'
Traceback (most recent call last):
  File "d:\Project\Engineering_Competency_Development\research-preparation\tracklab\W2\D5\file_frame.py", line 17, in read_widths
    record = parse_width(raw)
             ^^^^^^^^^^^^^^^^
  File "d:\Project\Engineering_Competency_Development\research-preparation\tracklab\W2\D5\file_frame.py", line 6, in parse_width
    width = float(fields[1])
            ^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'bad'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "d:\Project\Engineering_Competency_Development\research-preparation\tracklab\W2\D5\file_frame.py", line 30, in <module>
    result = read_widths(p)
             ^^^^^^^^^^^^^^
  File "d:\Project\Engineering_Competency_Development\research-preparation\tracklab\W2\D5\file_frame.py", line 20, in read_widths
    raise ValueError(message) from exc
ValueError: D:\Project\Engineering_Competency_Development\research-preparation\tracklab\W2\D5\width_demo.txt第2行无法解析，原文:'demo_b.jpg,bad'
"""