def main():
    dirtree = {}
    currentdir = ""
    file = open('7.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        if line.strip() == "$ cd /":
            currentdir = "/"
            dirtree[currentdir] = 0
        if line.startswith("$ cd") and "/" not in line and ".." not in line:
            dirname = line.strip().split("cd ")[1]
            if currentdir == "/":
                currentdir = currentdir + dirname
                dirtree[currentdir] = 0
            else:
                currentdir = currentdir + "/" + dirname
                dirtree[currentdir] = 0
        if line.strip() == "$ cd ..":
            splitted = currentdir.rsplit("/", 1)
            if splitted[0] == "":
                currentdir = "/"
            else:
                currentdir = splitted[0]
        if line[0].isdigit():
            size = int(line.strip().split(" ")[0])
            dirtree[currentdir] = dirtree[currentdir] + size
            parentdirs = currentdir
            if currentdir == "/":
                continue
            else:
                for x in range(currentdir.count("/")):
                    splitted = parentdirs.rsplit("/", 1)
                    if splitted[0] == "":
                        parentdirs = "/"
                        dirtree[parentdirs] = dirtree[parentdirs] + size
                    else:
                        parentdirs = splitted[0]
                        dirtree[parentdirs] = dirtree[parentdirs] + size

    dirsizes = [v for k,v in dirtree.items() if v <= 100000]
    print(sum(dirsizes))


if __name__ == "__main__":
    main()
