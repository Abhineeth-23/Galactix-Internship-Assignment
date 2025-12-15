txt = input("Enter your paragraph: ")

txt = txt.lower().replace("-", " ")

no_punctuation = ""

for a in txt:
    if a.isalnum() or a.isspace():
        no_punctuation += a

words = no_punctuation.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for x ,y in word_freq.items():
    print(f"'{x}': {y}")