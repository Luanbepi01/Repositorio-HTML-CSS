def check_a_in_string(s):
    count_lower = 0
    count_upper = 0
    for char in s:
        if char == 'a':
            count_lower += 1
        elif char == 'A':
            count_upper += 1

    if count_lower > 0:
        print(f"A letra 'a' minúscula aparece {count_lower} vezes na string.")
    else:
        print(f"A letra 'a' minúscula não aparece na string.")

    if count_upper > 0:
        print(f"A letra 'A' maiúscula aparece {count_upper} vezes na string.")
    else:
        print("A letra 'A' maiúscula não aparece na string.")

string = input("Informe uma string: ")
check_a_in_string(string)