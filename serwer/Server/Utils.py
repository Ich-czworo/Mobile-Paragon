from Server.Server import app


def seperate_articles(data):

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
        app.logger.info('%s Something went wrong in separating articles. Processing stopped.')
        return None

