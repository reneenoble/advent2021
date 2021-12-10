def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = [int(i) for i in list(line.strip())]
            data.append(line)
    return data

data = get_data("day3.txt")


def keep_data(data, bit, check_type):
    print("data", data)
    # sum_list = []
    # gamma = []
    # epsilon = []
    if len(data) == 1:
        return data[0]

    num = sum(binary[bit] for binary in data)
    
    if check_type == "o2":
        if num >= len(data) / 2:
            chosen = 1
        else:
            chosen = 0

    elif check_type == "co2":
        if num >= len(data) / 2:
            chosen = 0
        else:
            chosen = 1
    print("chosen", chosen)

    print(num, len(data))
    data = [d for d in data if d[bit] == chosen]
    print("d2", data)
    return keep_data(data, bit + 1, check_type)
        

o2 = "".join([str(i) for i in keep_data(data, 0, "o2")])
co2 = "".join([str(i) for i in keep_data(data, 0, "co2")])
dig_o2 = int(o2, 2)
dig_co2 = int(co2, 2)
print(dig_o2, dig_co2)
print(dig_o2 * dig_co2)



# gamma = "".join(gamma)
# epsilon = "".join(epsilon)



    # g = int(gamma, 2)
    # e = int(epsilon, 2)
    # print(g*e)
