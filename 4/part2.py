def main():
    containing_pairs = 0
    file = open('4.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        pair_split1 = line.strip().split(",")[0]
        pair_split2 = line.strip().split(",")[1]
        digit_split1 = pair_split1.split("-")
        digit_split2 = pair_split2.split("-")
        digit1 = int(digit_split1[0])
        digit2 = int(digit_split1[1])
        digit3 = int(digit_split2[0])
        digit4 = int(digit_split2[1])
        firstrange = range(digit1, digit2 + 1)
        secondrange = range(digit3, digit4 + 1)
        if len(firstrange) > len(secondrange):
            for i in secondrange:
                if digit1 <= i <= digit2:
                    containing_pairs += 1
                    break
        else:
            for i in firstrange:
                if digit3 <= i <= digit4:
                    containing_pairs += 1
                    break
    print(containing_pairs)


if __name__ == "__main__":
    main()