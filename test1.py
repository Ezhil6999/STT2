import nltk
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
# used for posting the tag weaher it is object, adjective,verb amd so on
a=tagged[0:6]
print(a)