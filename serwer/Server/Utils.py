
def seperate_articles(data):
    pocz = None
    kon = None

    # szukamy słów "paragon fiskalny" oraz "suma"
    for (index, word) in enumerate(data):
        if word == 'fiskalny':
            pocz = index

        if word == 'suma':
            kon = index

    if kon and pocz and pocz < kon:
        print("pocz: ", pocz, "kon: ", kon)
        return data[pocz + 1:kon]
    else:
        return None

