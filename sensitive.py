import pandas as pd

# some multiples due to the possibility of similar looking but different characters
sensitive_words = ['bitch', 'bitches', 'nigga', 'niggas', 'pussy', 'slut', 'hoe', 'bitches', 'pussys', 'fuck', 'ass', 
                   'damn', 'dick', 'fucking', 'fuckin', 'motherfuckin', 'fucking', 'fucking', 'bitch', 'bitch']

words_ser = pd.Series(sensitive_words)

words_ser.to_csv("sensitive_words.csv")
