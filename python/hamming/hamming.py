def distance(strands1,strands2):
    pots = 0
    if len(strands1) != len(strands2):
        return False
    else:
        for n in range(len(strands1)):
            if strands1[n] != strands2[n]:
                pots += 1
    return pots
