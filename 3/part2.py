def main():
    sum_of_priorities = 0
    file = open('3.txt', 'r')
    Lines = file.readlines()
    for line in Lines[::3]:
        group1 = line.strip()
        group2 = Lines[Lines.index(line) + 1].strip()
        group3 = Lines[Lines.index(line) + 2].strip()
        common_item = (next(iter(set(group1) & set(group2) & set(group3))))
        if common_item.isupper():
            sum_of_priorities += ord(common_item) - 38
        else: 
            sum_of_priorities += ord(common_item) - 96
    print(sum_of_priorities)

    
if __name__ == "__main__":
    main()