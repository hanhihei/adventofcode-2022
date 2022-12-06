def main():
    # stacks are hand-written into lists and removed from input file
    stack1 = ["W", "M", "L", "F"]
    stack2 = ["B", "Z", "V", "M", "F"]
    stack3 = ["H", "V", "R", "S", "L", "Q"]
    stack4 = ["F", "S", "V", "Q", "P", "M", "T", "J"]
    stack5 = ["L", "S", "W"]
    stack6 = ["F", "V", "P", "M", "R", "J", "W"]
    stack7 = ["J", "Q", "C", "P", "N", "R", "F"]
    stack8 = ["V", "H", "P", "S", "Z", "W", "R", "B"]
    stack9 = ["B", "M", "J", "C", "G", "H", "Z", "W"]
    stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    file = open('5.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        move_amount = int(line.strip().split(" ")[1].split(" ")[0])
        move_from = int(line.strip().split("from ")[1].split(" ")[0])
        move_to = int(line.strip().split("to ")[1])
        stacklength = len(stacks[move_from - 1])
        for n in range(move_amount):
            stacks[move_to - 1].append(stacks[move_from - 1][stacklength - move_amount])
            del stacks[move_from - 1][stacklength - move_amount]
        

    for stack in stacks:
        print(stack.pop())


if __name__ == "__main__":
    main()
