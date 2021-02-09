n = int(input("Enter Feet:"))
if n<1000:
    print("Safe to land")
elif n>1000 and n<5000:
    print("Bring down to 1000")
elif n>5000:
    print("Turn Around")