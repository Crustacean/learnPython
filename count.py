import sys
sys.set_int_max_str_digits(0)

print("Started job ...")

total = 1

for num in range(1,1000000000000000000):
    print(total)
    total = total * num * num
print("Final result")
print(total)
print("...job ended.")


try:

except:

file = open("ping.txt")
lines = file.readlines()

time_list = []
time_set = set()

for line in lines:
    values = line.split(" ")
    time = values[4]
    sec = time.split("=")
    ms = sec[1]
    s = ms[0:2]
    time_list.append(s)
    time_set.add(s)

time_list.sort(reverse=True)  
print(time_list)
print(sorted(time_set))