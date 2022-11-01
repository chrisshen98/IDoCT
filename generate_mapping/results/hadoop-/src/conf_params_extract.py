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
toWrite = "{\n"
for item in testClasses:
    toWrite += "\t"+item+"\n"
    print(item)
    print("\n")
toWrite += "}"
f = open("../test_class_list.json", "w")
f.write(toWrite)
f.close()

print("\n"+"Test methods:"+"\n")
toWrite = "{\n"
for item in testMethods:
    toWrite += "\t"+item+"\n"
    print(item)
toWrite += "}"
f = open("../test_method_list.json", "w")
f.write(toWrite)
f.close()