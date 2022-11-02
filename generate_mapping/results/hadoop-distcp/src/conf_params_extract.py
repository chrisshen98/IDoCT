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
            msg = "\""+tempClass+"\""
            if msg  not in testClasses:
                testClasses.append("\""+tempClass+"\"")
        elif "("+tempClass+")" in line:
            temp = line.split("("+tempClass+")")[0]
            testMethod = temp.split("] ")[1]
            testMethod = testMethod.split("[")[0]
            msg = "\""+tempClass+"#"+testMethod+"\""
            if msg not in testMethods:
                testMethods.append(msg)
            
print("\n"+"Test classes:"+"\n")
toWrite = "["
first = True
for item in testClasses:
    if not first:
        toWrite += ","
    first = False
    toWrite += "\n"+"\t"+item
    # print(item)
    # print("\n")
toWrite += "\n]"
f = open("../test_class_list.json", "w")
f.write(toWrite)
f.close()

print("\n"+"Test methods:"+"\n")
toWrite = "["
first = True
for item in testMethods:
    if not first:
        toWrite += ","
    first = False
    toWrite += "\n"+"\t"+item
    # print(item)
toWrite += "\n]"
f = open("../test_method_list.json", "w")
f.write(toWrite)
f.close()