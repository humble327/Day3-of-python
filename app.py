# ans = input("Whats Ur Name? ")
# print("hello " + ans)

# using formatted string
# ans = input("Whats Ur Name? ")
# print("hello {ans}")

# ans = input("Whats Ur Name? ")
# print(f"hello {ans}")

# increment by 1
# counter = 2
# counter += 1
# print(counter)

# num = input("input Number")
# num2 = input("input Number")
# solu = "number"
# if num > num2:
#     print(f"{num} is greater")
# elif num < num2:
#     print(f"{num} is less ")
# else:
#     print(f"{num} is less than the given " + solu )


# Loop {While Loop}
# i = 0
# while i < 3:
#     print("hello world")
#     i += 1

# for i in range(11234567890):
#     print(i)

from PIL import Image,ImageFilter
before = Image.open("shark.png")
after = before.filter(ImageFilter.BoxBlur(12))
after.save("out.png")