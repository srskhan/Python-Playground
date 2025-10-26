words = ["sun", "planet", "moon", "star", "universe"]

words_greater_than_four = list(filter(lambda x:len(x)>4, words))
print(words_greater_than_four)