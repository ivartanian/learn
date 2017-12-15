a = "Hello2"
b = "Hello1"

if a == b:
    print("True")
elif a > b:
    print("Test")
else:
    print("False")

c = True
iterator = 1
while c:
    print(c)
    print(iterator)
    if iterator > 100:
        c = False
    iterator += 1
else:
    print("Finish")

for i in range(1, 10):
    print(i)
else:
    print("Finish For")