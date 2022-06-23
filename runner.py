from SVO_extraction import findSVOs, nlp
ques = input()
tokens = nlp(ques)
svos = findSVOs(tokens)
print(svos)
