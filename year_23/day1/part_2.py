def is_letter_number(letter):
    if len(letter) == 3:
        match letter:
            case 'one':
                return 1
            case 'two':
                return 2
            case 'three':
                return 3
            case 'four':
                return 4
            case 'five':
                return 5
            case 'six':
                return 6
            case 'seven':
                return 7
            case 'eight':
                return 8
            case 'nine':
                return 9


    match letter:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9


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
