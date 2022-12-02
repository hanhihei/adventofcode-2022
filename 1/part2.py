def main():
    # read input file, add lines to a list:
    file = open("1.txt", "r")
    Lines = file.readlines()
    # create variables:
    most_calories = 0
    second_most_calories = 0
    third_most_calories = 0
    current_elf_calories = 0
    # loop through lines, check if an elf is top3 at blank space
    for line in Lines:
        if line.strip():
            current_elf_calories += int(line)
        elif current_elf_calories > most_calories:
            third_most_calories = second_most_calories
            second_most_calories = most_calories
            most_calories = current_elf_calories
            current_elf_calories = 0
        elif current_elf_calories > second_most_calories:
            third_most_calories = second_most_calories
            second_most_calories = current_elf_calories
            current_elf_calories = 0
        elif current_elf_calories > third_most_calories:
            third_most_calories = current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories = 0
    print(most_calories
          + second_most_calories 
          + third_most_calories)


if __name__ == "__main__":
    main()