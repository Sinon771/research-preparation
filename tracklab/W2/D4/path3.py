r"""
执行到 mkdir() 才会真正创建目录：
- parents=True：缺少上级目录时，一起创建。
- exist_ok=True：目标目录已存在时，允许继续，方便重复运行。
- 如果同名位置已经是一个普通文件，仍然会报错；它不会把文件转换成目录
"""

from pathlib import Path

base = Path("D:/Project/Engineering_Competency_Development/research-preparation/tracklab/W2/D4")
folder = base / "image_samples"

folder.mkdir(parents=True, exist_ok=True)

print(folder)
print(folder.is_dir())