with open('input.txt', 'r') as file:
    input = file.read()

    sum_num = 0
    for line in input.splitlines():
        line = line.strip()
        i = -1
        j = len(line)
        first_digit = -1
        second_digit = -1
        while i <= len(line) - 1:
            try:
                i += 1
                if first_digit == -1:
                    first_digit = int(line[i])
                else:
                    break
            except ValueError:
                pass

        while j >= 0:
            try:
                j -= 1
                if second_digit == -1:
                    second_digit = int(line[j])
                else:
                    break
            except ValueError:
                continue

        sum_num += (first_digit * 10) + second_digit

    print(sum_num)
