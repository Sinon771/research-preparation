r"""
1. / 用于拼接路径
image = root / "demo_mnist_grid.png"
当左边是 Path 对象时，`/` 表示连接路径组件。可以连续连接：
script = root / "tracklab" / "W2" / "D4" / "path.py"
它们都只是在构造路径，不会创建目录或文件，也不会切换工作目录。`root` 本身也不会被修改，拼接得到的是新的路径对象。

注意，后面的组件应使用相对形式；如果传入另一个完整绝对路径，前面的路径会被替换。

2. Windows 路径字符串可以使用 /

示例使用正斜杠，避免普通字符串中的 \n、`\t` 被解释为换行、制表符。使用反斜杠时，可以写原始字符串：
root = Path(r"D:\Project\Engineering_Competency_Development\research-preparation")
这里的 r 让反斜杠按字面保留。

3. 路径对象可以提供文件名和后缀
image.name
image.suffix
name 是最后一个路径组件，`suffix` 是最后一个扩展名，包含开头的点。

4. parent 获取父路径
image.parent
这些是属性，直接访问；
"""
from pathlib import Path

root = Path("D:/Project/Engineering_Competency_Development/research-preparation")
image = root / "demo_mnist_grid.png"


print(root)
print(image)
print(image.name)
print(image.suffix)
print(image.parent)
print(image.is_file())

for entry in root.iterdir():
    print(entry.name,entry.is_file(),entry.is_dir())