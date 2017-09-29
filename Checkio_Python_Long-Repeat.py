def long_repeat(line):
    letter = ''
    max_count = 0
    for index in line:
        letter = index
        count = 0
        for indexed in line:
            if indexed == letter:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                 count = 0
    return max_count
