def main():
    file = open('6.txt', 'r')
    input = file.read()
    startindex = 0
    endindex = 4
    for n in range(len(input)):
        if len(set(input[startindex:endindex])) == len(input[startindex:endindex]):
            print(endindex)
            break
        else:
            startindex += 1
            endindex += 1
    

if __name__ == "__main__":
    main()
