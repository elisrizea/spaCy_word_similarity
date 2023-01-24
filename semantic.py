# Import module and models
import spacy

nlp_ms = spacy.load('en_core_web_sm')
nlp_md = spacy.load('en_core_web_md')

# Ccolors as const for a better console print
GREEN = '\033[92m'
END = '\033[0m'

# Request user to input tha list of words or use default
words_list = input('Please input a list of words separated by coma or type "n" to use the default list:')
words_list = words_list.split(",")
if len(words_list) <= 1:
    words_list = ['cat', 'monkey', 'rabbit', 'car', 'toyota', 'diesel', 'banana', 'apple', 'orange', 'tree', 'wood',
                  'gsvrega']
else:
    for i in range(len(words_list)):
        words_list[i] = words_list[i].strip().lower()


# Compare all words in the list among each-other and print the similarity score using
# the model "en_core_web_sm" and "en_core_web_md" as percentage.
# In the end print the difference between models as percentage
average_diff, c = 0, 0

for token in words_list:
    token_md = nlp_md(token)
    token_sm = nlp_ms(token)

    for token_ in words_list:
        token_md_ = nlp_md(token_)
        token_sm_ = nlp_ms(token_)
        similarity_sm = token_sm.similarity(token_sm_)
        similarity_md = token_md.similarity(token_md_)
        sim_sm_proc = round(similarity_sm * 100)
        sim_md_proc = round(similarity_md * 100)
        c += 1
        average_diff += similarity_sm - similarity_md

        print(f'\n* For {GREEN}{token_sm.text}{END} and {GREEN}{token_md_.text}{END} the similarity score is:\n '
              f'{GREEN}{sim_sm_proc}%{END} for en_core_web_sm and {GREEN}{sim_md_proc}%{END} for en_core_web_md => '
              f'(SM vs MD score is {sim_sm_proc - sim_md_proc}%)')

print(f'\nAverage difference is {round(average_diff * 100 / c)}% en_core_web_sm vs en_core_web_md')

# **************************************************** My conclusions **********************************************
# On the sets of words I use the average dih between "en_core_web_sm" and "en_core_web_md" tends to vary from 30% to 40%
# "en_core_web_md" have over all better results but the fluctuation in consistency is big for both models
# "en_core_web_sm" throw a bigger number of warnings then "en_core_web_md"
# If your experience is different  using this test please let me know
# Important notice when we use a string that is not a word "en_core_web_md" result is 0% similarity with other words,
# "en_core_web_sm" will try to guess similarities with other words
# ******************************************************************************************************************
