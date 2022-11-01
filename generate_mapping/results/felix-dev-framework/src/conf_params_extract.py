files = ["test.log"]
params = []
testClasses = []
for file in files:
    with open(file) as f:
        f = f.readlines()
    for line in f:
        if "[CTEST]" in line:
            # print(line)
            param = line.split(" ")[1]
            # print(param)
            if param not in params:
                params.append(param)
        if "Running" in line:
            temp = line.split("Running ")[1]
            path = temp.split("")[0]
            testClass = temp.split("")[1].split("1m")[1]
            testClasses.append("\""+path+testClass+"\",")
for item in params:
    print(item)
print("\n")
for item in testClasses:
    print(item)
    print("\n")