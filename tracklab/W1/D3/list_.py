scores = [60, 75, 90]

scores[0] = 80
print(scores)
print(len(scores))

t=scores.append(95)
print(scores,t)#[80, 75, 90, 95] None
print(scores[-1])

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:5:2])
print(numbers[5:0:-2])
print(numbers[::-2])#[60, 40, 20]
print(numbers[4:1])