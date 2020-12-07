f = open("input.txt")
raw_data = f.read().split("\n")

for x in raw_data:
    if (x.strip() == ""):
        continue
    for y in raw_data:
        if y.strip() == "":
            continue
        for z in raw_data:
            if z.strip() == "":
                continue
            
            if int(x) + int(y) + int(z) == 2020:
                print(x)
                print(y)
                print(z)
                print(int(x)*int(y)*int(z))
                quit()