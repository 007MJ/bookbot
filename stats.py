def get_num_words(text):
    dict_words = {}
    for c in text.lower():
        if not c in dict_words:
            dict_words[c] = text.lower().count(c)
    dict_words = dict(sorted(dict_words.items(), key=lambda item: item[1], reverse=True))
    return dict_words