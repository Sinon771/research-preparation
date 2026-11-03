from pathlib import Path

root = Path("D:/Project/Engineering_Competency_Development/research-preparation/tracklab/W2/D4")
folder_path = root / "image_samples"

def inspect_image_dir(folder):
    folder = Path(folder)
    dic={
        "image_names":[],
        "image_count":0,
        "subdir_count":0,
    }
    for item in folder.iterdir():
        allowed =(".jpg",".jpeg",".png")
        if item.is_file() and item.suffix.lower() in allowed:
            dic["image_count"]+=1
            dic["image_names"].append(item.name)
        if item.is_dir():
            dic['subdir_count']+=1
    return dic

result=inspect_image_dir(folder_path)
result_empty=inspect_image_dir(root/"empty_samples")
print(result)
print(result_empty)

"""
{'image_names': ['0001.jpg', '0002.jpg', '0003.jpg', '0004.jpg', '0005.jpg', '0006.jpg', '0007.jpg', '0008.jpg', '0009.jpg', '0010.jpg', '0011.jpg', '0012.jpg', '0013.jpg', '0014.jpg', '0015.jpg', '0016.jpg', '0017.jpg', '0018.jpg', '0019.jpg', '0020.JpG'], 'image_count': 20, 'subdir_count': 2}
{'image_names': [], 'image_count': 0, 'subdir_count': 0}
"""