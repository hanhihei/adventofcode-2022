def main():
    sum_of_priorities = 0
    file = open('3.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        slicer1 = slice(0, len(line) // 2)
        slicer2 = slice(len(line) // 2, len(line)) 
        compartment1 = line[slicer1].strip()
        compartment2 = line[slicer2].strip()
        common_item = next(iter(set([*compartment1]).intersection([*compartment2])))
        if common_item.isupper():
            sum_of_priorities += ord(common_item) - 38
        else: 
            sum_of_priorities += ord(common_item) - 96
    print(sum_of_priorities)


if __name__ == "__main__":
    main()