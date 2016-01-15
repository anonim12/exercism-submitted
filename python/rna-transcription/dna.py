def to_rna(strands):
    shift = {"G":"C", "C":"G", "T":"A", "A":"U"}
    pods = ""

    for nucleotides in strands:
        pods += shift.get(nucleotides,"X")
    return pods
