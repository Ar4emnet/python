def snail(snail_map):
    m = []
    while len(snail_map) != 0:
        m += snail_map[0]
        del (snail_map[0])
        for n in range(len(snail_map) - 1):
            m += [snail_map[n][-1]]
            del snail_map[n][-1]

        if len(snail_map) == 0:
            return m
        m += snail_map[-1][::-1]
        del (snail_map[-1])
        for n in snail_map[::-1]:
            m += [n[0]]
            del (n[0])
        if len(snail_map) == 0:
            return m
    return m


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))

print(snail([[1,2,3],[5,6,7],[8,9,10]]))        
        

        