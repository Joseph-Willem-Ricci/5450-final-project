import pandas as pd

sensitive_words = ['bitch', 'nigga', 'niggas', 'pussy', 'slut', 'hoe', 'bitches', 'pussys', 'fuck', 'ass', 'damn','dick']

words_ser = pd.Series(sensitive_words)

words_ser.to_csv("sensitive_words.csv")
