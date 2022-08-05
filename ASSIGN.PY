# CLASSWORK
# CHECK WHETHER 10 IS GREATER OR LESS THAN 1
# USING CONDITION

z = input("subject name: ")
m = input("book name:  ")

z = int(z)
m = int(m)

if z > m:
    print ("z is greater than m!")
    if z >= 10:
        print("z is negative1")
    else:
        print("z is positive!")
if z < m:
    print("z is less than m!")
    if z < 10:
        print("z is less than 10")
else:
    print("zis equal to m")