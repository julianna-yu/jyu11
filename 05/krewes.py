# Julianna Yu (with Ruoshui Mao & Cindy Zheng)
# SoftDev
# K05: Teamwork, but Better This Time
# 09/30/2020

KREWES = {
   'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
   'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
   'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

def random_name():
    import random
    all_names = []
    total = len(KREWES.get("orpheus")) + len(KREWES.get("rex")) + len(KREWES.get("endymion"))
    for i in range(total):
        if (i < len(KREWES.get("orpheus"))):
            all_names.append(KREWES.get("orpheus")[i])
        elif (i < len(KREWES.get("orpheus")) + len(KREWES.get("rex"))):
            all_names.append(KREWES.get("rex")[i - len(KREWES.get("orpheus"))])
        else:
            all_names.append(KREWES.get("endymion")[i - (len(KREWES.get("orpheus")) + len(KREWES.get("rex")))])
    i = random.randint(0, total - 1)
    return (all_names[i])

if __name__ == "__main__":
    print(random_name())
