import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_properties(0).total_memory/1e9) 

"""
Output:
2.4.0
True
11.8
NVIDIA GeForce RTX 3050 Laptop GPU
4.294443008
"""