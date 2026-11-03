sample = {
    "frame": "401.jpg",
    "box": [10, 20, 16, 12],
    "visible": True,
}
def shift_sample(sample,dx,dy,history=None):
    s = sample.copy()
    s["box"]=sample["box"].copy()
    s["box"][0]+=dx
    s["box"][1]+=dy
    if history==None:
        s["history"]=[]
    else:
        s["history"]=history
    s["history"].append(sample["frame"])
    return s
result = shift_sample(sample, 5, -3)
print(sample)
print(result)
