with open("client.html", "r") as f:
    for line in f.readlines():
        if "{target_name}" in line:
            line = line.replace("{target_name}", "Baani")
            print(line)