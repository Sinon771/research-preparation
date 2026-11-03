def collect_frame(frame, frames=[]):
    frames.append(frame)
    return frames

first = collect_frame("001.jpg")
second = collect_frame("002.jpg")

print(first)
print(second)