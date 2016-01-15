def word_count(phrase):
    phrase = phrase.decode('utf-8')
    phrase = ''.join(c if c.isalnum() else ' ' for c in phrase)
    list = {}
    for n in phrase.lower().split():
        if n in list.keys():
            list[n] += 1
        else:
            list[n] = 1
    return list
