
#1
file = open("data.txt")

#2
# print(type(file))
data = file.read()
print(f'print before closed\n  {data}')
#3
file.close()
print('\n')
print(data)

def is_closed(file_):
    if file_.closed:
        print("File closed")
    else:
        print("File opened")

with open("data.txt") as file:
    print(type(file))
    data = file.read()
    print(data)
    is_closed(file)

is_closed(file)

with open("data2.txt") as file:
    data = file.readlines()
    print(type(data))
    print(data)
    print(len(data))
    print(data[2])
    for i in data:
        print(i.strip())
print("\n")

with open("data2.txt") as file:
    file.readline()
    for line in file:
        print(line.strip())
        if line.strip() == "arepo":
            data_ = file.readline()
            print(f"SKIP - {data_.strip()}")

with open("data3.txt", "w") as file:
    file.write("PER ASPERA AD ASTRA")
with open("data3.txt", "a") as file:
    file.write("\nOKKAM GLADIUS")

with open("data3.txt", "rb") as file:
    data = file.read()
    print(type(data))
    print(data)


