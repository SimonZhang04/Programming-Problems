num_list = []


for x in range(int(input())):
  num_list.append(int(input()))

num_list.sort()
for x in range(len(num_list)):
  print(num_list[x])