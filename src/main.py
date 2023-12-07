def max_experience(levels, experience):
    levels_of_collected_exp = []
    for i in range(levels):
        row = []
        for j in range(i + 1):
            row.append(0)
        levels_of_collected_exp.append(row)
    for i in range(levels):
        current_level_experience = experience[i]
        for j in range(i + 1):
            if j > 0:
                levels_of_collected_exp[i][j] = current_level_experience[j] + max(levels_of_collected_exp[i - 1][j - 1], 0)
            elif j < i:
                levels_of_collected_exp[i][j] = current_level_experience[j] + max(levels_of_collected_exp[i - 1][j], 0)
            else:
                levels_of_collected_exp[i][j] = current_level_experience[j]
    return max(levels_of_collected_exp[-1])


def read_and_write(input_path, output_path):
    with open(input_path, 'r') as file:
        levels = int(file.readline().strip())
        experience = []
        for _ in range(levels):
            line = file.readline().strip().split()
            row = [int(element) for element in line]
            experience.append(row)
    result = max_experience(levels, experience)
    with open(output_path, 'w') as file:
        file.write(str(result))
