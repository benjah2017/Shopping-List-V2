lines = open("README.MD", "r").readlines()

for line in lines:
    print(line, end="")

print("\nEverything is OK")