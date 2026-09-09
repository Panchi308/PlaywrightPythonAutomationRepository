odd =[]
for i in range(20,41):
    if(i % 2 ==1):
        odd.append(i)
print(odd)
# print numebrs which are divisible by 3
for item in odd:
    if(item % 3 ==0):
        print(item)