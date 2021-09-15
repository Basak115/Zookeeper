group1 = abs(int(input()))
group2 = abs(int(input()))
group3 = abs(int(input()))
class1 = group1 // 2 + group1 % 2
class2 = group2 // 2 + group2 % 2
class3 = group3 // 2 + group3 % 2
descs = class1 + class2 + class3
print(descs)
