files = ["test.log"]
testClasses = []
testMethods = []
tempClass = ""
for file in files:
    with open(file) as f:
        f = f.readlines()
    for line in f:
        if "Running" in line:
            temp = line.split("Running ")[1]
            path = temp.split("")[0]
            testClass = temp.split("")[1].split("1m")[1]
            tempClass = path+testClass
            testClasses.append("\""+tempClass+"\",")
        elif "("+tempClass+")" in line:
            temp = line.split("("+tempClass+")")[0]
            testMethod = temp.split("] ")[0]
            testMethods.append(tempClass+"#"+testMethod)
print("\n"+"Test classes:"+"\n")
for item in testClasses:
    print(item)
    print("\n")

print("\n"+"Test methods:"+"\n")
for item in testMethods:
    print(item)