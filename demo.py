
input1 = int(input("এখনে একটা নাম্বার দেন: "))
input2 = int(input("এখনে আরও একটা নাম্বার দেন: "))

a = [input1,input2]

for i in a:
    #print(i)
    for j in range(1,11):
        b = i * j
        print(f"{i} * {j} = {b}")
    print()

a = (2,2,1,5,4,6,7,4,3,1,7,8)
print(type(a),a)
b = list(a)
b.sort()
print(b)
print(f"Max number of alist : {(b[len(b)-1])}")
print(f"2nd Max number of alist : {(b[len(b)-2])}")
print(f"3rd Max number of alist : {(b[len(b)-3])}")

a = int(input("Enter A Number :"))

for i in range(1,a*2,2):
    for j in range(1,i+1):

        print( "*" , end='')
    print()

print()

for i in range(1,a+1):
    for j in range(1,i+1):

        print( j, end='')
    print()

for i in range(a-1,0,-1):
    for j in range(1, i + 1):
        print(j, end='')
    print()