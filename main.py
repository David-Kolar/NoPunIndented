from copy import deepcopy
def load_input(path="vstup"):
    with open(path) as vstup:
        first = True
        new = []
        for line in vstup:
            line = line.strip()
            if not(first):
                if (line[-1]==":"):
                    new.append(True)
                else:
                    new.append(False)
            first = False
        return new

def output(comb):
    with open("output", "w") as file:
        file.write(str(comb))

def make_array(inp):
    l = len(inp)
    data = []
    for _ in range(l):
        data2 = []
        for _ in range(l):
            data2.append(0)
        data.append(data2)
    return data

# exponencialni slozitost
def recursive_solution(idx=0, inp=[], level=1):
    if (data[idx][level] > 0):
        return data[idx][level]

    comb = 0
    while(True):
        line = inp[idx]
        if not(line):
            break
        level += 1
        idx += 1
    if ((len(inp)-idx-1)<=0):
        return 1

    for lvl in range(1, level+1):
        comb += recursive_solution(idx+1, inp, lvl)
    data[idx][level] = comb
    return comb

# O(n**3)
def polynomal_solutionV1(inp):
    pomocne_pole = [0 for _ in range(len(inp))]
    pomocne_pole[0] = 1
    prime = 10**9 + 7
    old = []
    for idx, line in enumerate(inp):
        print(pomocne_pole)
        nove_pole = [0 for _ in range(len(inp))]
        old = deepcopy(pomocne_pole)
        if (line):
            for key in range(idx+1):
                nove_pole[key+1] = pomocne_pole[key]
            pomocne_pole = deepcopy(nove_pole)
        else:
            for key in range(idx+1):
                for key2 in range(0, key):
                    pomocne_pole[key2] = (pomocne_pole[key2] + pomocne_pole[key])

    return sum(old) % prime

# O(n**2) - vylepšeno průběžnými součty
def polynomal_solutionV2(inp):
    pomocne_pole = [0 for _ in range(len(inp))]
    pomocne_pole[0] = 1
    prime = 10**9 + 7
    old = []
    for idx, line in enumerate(inp):
        nove_pole = [0 for _ in range(len(inp))]
        old = deepcopy(pomocne_pole)
        if (line):
            for key in range(idx+1):
                nove_pole[key+1] = pomocne_pole[key]
            pomocne_pole = deepcopy(nove_pole)
        else:
            soucet = 0
            for key in range(idx+1):
                soucet += pomocne_pole[key]
            for key in range(idx+1):
                soucet -= pomocne_pole[key]
                pomocne_pole[key] = (pomocne_pole[key] + soucet) % prime

    return sum(old) % prime


inp = load_input("vstup")
data = make_array(inp)
comb = polynomal_solutionV2(inp)
print(comb)
output(comb)
