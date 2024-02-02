while True:
    num = input('Skriv nummer här: ').split()
    if num[0].lower() == "end":
        break
    numInput = list(map(float, num))

    if len(num) >= 3:
        for i in range(len(num)):

            if i != 0 and i != len(num) -1:
                avg = (numInput[i] + numInput[i + 1] + numInput[i - 1]) / 3
                print(avg)
            else:
                print(numInput[i])
            