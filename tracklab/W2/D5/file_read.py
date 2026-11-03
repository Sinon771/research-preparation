from pathlib import Path

base =Path("D:/Project/Engineering_Competency_Development/research-preparation/tracklab/W2/D5")
p= base/"text_demo.txt"
with open(p,"w",encoding="utf-8") as f:
    f.write("第一行\n第二行\n")
with open(p,"r",encoding="utf-8") as f:
    text=f.read()
    rest=f.read()
print(repr(text))
print(repr(rest))
print(f.closed)
