files = ["test_class_list.json"]
testClasses = []
for file in files:
    with open(file) as f:
        f = f.readlines()
    for line in f:
        if "\"" in line:
            testClasses.append(line.split("\"")[1])
files = []
for c in testClasses:
    files.append(c+"-output.txt")
params = []
for file in files:
    try:
        f = open(file)
        f = f.readlines()
        for line in f:
            if "[CTEST]" in line:
                param = line.split(" ")[1]
                if param not in params:
                    params.append(param)
    except IOError:
        print("")
toWrite = ""
for item in params:
    toWrite += item+"\n"
    print("item")
# print(toWrite)
f = open("conf_params.txt", "w")
f.write(toWrite)
f.close()
