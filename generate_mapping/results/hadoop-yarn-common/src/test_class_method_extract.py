files = ["test.log"]
testClasses = []
testMethods = []
tempClass = ""
for file in files:
    with open(file) as f:
        f = f.readlines()
    for line in f:
        if "[INFO] Running" in line:
            tempClass = line.split("Running ")[1]
            tempClass = tempClass[:-1]
            msg = "\""+tempClass+"\""
            if msg  not in testClasses:
                testClasses.append(msg)
        if "[INFO] org" in line:
            fullLine = line.split(" ")[1]
            method = fullLine.split(tempClass+".")[1]
            msg = "\"" + tempClass + "#" + method +"\""
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