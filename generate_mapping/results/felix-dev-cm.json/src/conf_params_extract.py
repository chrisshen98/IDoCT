files = ["test.log"]
params = []
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
print(params)