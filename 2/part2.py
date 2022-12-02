def rps_battle(hands):
    if hands[0] == "A" and hands[1] == "X":
        return 0, 3
    if hands[0] == "A" and hands[1] == "Y":
        return 3, 1
    if hands[0] == "A" and hands[1] == "Z":
        return 6, 2
    if hands[0] == "B" and hands[1] == "X":
        return 0, 1
    if hands[0] == "B" and hands[1] == "Y":
        return 3, 2
    if hands[0] == "B" and hands[1] == "Z":
        return 6, 3
    if hands[0] == "C" and hands[1] == "X":
        return 0, 2
    if hands[0] == "C" and hands[1] == "Y":
        return 3, 3
    if hands[0] == "C" and hands[1] == "Z":
        return 6, 1

def main():
    total_score = 0
    file = open('2.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        splitted = line.strip().split(" ")
        fight_result = rps_battle(splitted)
        total_score += fight_result[0] + fight_result[1]
    print(total_score)

if __name__ == "__main__":
    main()