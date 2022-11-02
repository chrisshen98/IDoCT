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
err = 0
for file in files:
    try:
        f = open(file)
        f = f.readlines()
        for line in f:
            if line.startswith("[CTEST]"):
                param = line.split(" ")[1]
                if param not in params:
                    params.append(param)
    except IOError:
        err+=1
toWrite = ""
for item in params:
    toWrite += item+"\n"

lines = toWrite.split('\n')
lines = [line for line in lines if line.strip()]
toWrite = ""
for line in lines:
    toWrite += line+"\n"
# print(toWrite)
f = open("conf_params.txt", "w")
f.write(toWrite)
f.close()
