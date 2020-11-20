with open('zarplata.txt', 'r', encoding='utf-8') as zar_file:
    z_dict = {line.split()[0]: float(line.split()[1]) for line in zar_file}
    print(z_dict)

    med_z = sum(z_dict.values()) / len(z_dict)
    zar_lit = [i[0] for i in z_dict.items() if i[1] < 20000]
    print(med_z)
    print(zar_lit)
