"""
Path.cwd()：获取当前工作目录的完整路径，返回一个路径对象。
p.resolve()：返回解析后的绝对路径。对于这里的相对路径，它以工作目录为起点；如果 p 已是绝对路径，就不再把工作目录接到前面。得到绝对路径不代表文件存在。
p.is_file()：检查路径是否指向一个实际存在的普通文件。不存在或指向目录时，都返回 False。
"""
from pathlib import Path

p = Path("demo_mnist_grid.png")

print(Path.cwd())
print(p)
print(p.resolve())
print(p.is_file())


