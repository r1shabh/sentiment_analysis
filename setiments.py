
positive_words = []
negative_words = []


def word_frequency(document):
    freq = {}
    words = document.split()
    for word in words:
        if word in freq:
            freq[words] += 1
        else:
            freq[words] = 1
    return freq
