file:str = "未命名.md"
temp_file:str = "temp.md"

with open(file, "r", encoding="utf-8") as f:
    content = f.readlines()

with open(temp_file, "w", encoding="utf-8") as f:
    for line in content:
        if line.startswith("\n"):
            pass
        else:
            f.write(line)
