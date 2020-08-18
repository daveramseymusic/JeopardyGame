import pandas as pd
import random as rd
import datetime as dt
jeopardy = pd.read_csv('jeopardy.csv')

pd.set_option('display.max_colwidth', None)

#clean columns

jeopardy.columns = jeopardy.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

my_words = ['computer']

#turn all 'value' column things to float
jeopardy['value'] = jeopardy['value'].apply(lambda x: x.replace('$', '').replace(',', '').replace('None','0')\
                                            if isinstance(x, str)\
                                            else x)\
                                            .astype(float)


def data_filter(df,search_words):
#     # make all words lowercase and decide if the word is there.
    filter = lambda x: all(word.lower() in x.lower() for word in search_words)
    #set it up so you release a row at a time if filter is true when going through each row in 'qs'
    return df.loc[df['question'].apply(filter)]


#oughts_filtered_questions = data_filter(oughts, my_words)


##ask which decade they'd prefer: 80's 90s 2000 or 2010s?
#if ask 2000
# decade = input('which decade of jeopardy would you prefer: 1980s 1990s 2000 or 2010s? reply with format YYYY: ---->')
# df['date'] = df.air_date.apply(lambda x: pd.to_datetime(x))
#     #use it later like this
#     filtered_by_computer_80s = filtered_by_computer[(filtered_by_computer.date > datetime.datetime(1989, 1, 1)) & (filtered_by_computer.date <= datetime.datetime(1989, 12, 31))]
#     filtered_by_computer_90s = filtered_by_computer[(filtered_by_computer.date > datetime.datetime(1990, 1, 1)) & (filtered_by_computer.date <= datetime.datetime(1999, 12, 31))]
#     filtered_by_computer_00s = filtered_by_computer[(filtered_by_computer.date > datetime.datetime(2000, 1, 1)) & (filtered_by_computer.date <= datetime.datetime(2000, 12, 31))]
#     filtered_by_computer_10s = filtered_by_computer[(filtered_by_computer.date > datetime.datetime(2010, 1, 1)) & (filtered_by_computer.date <= datetime.datetime(2010, 12, 31))]
#use function if show number is = random int then print question
# x = rd.randint(jeopardy.show_number.min(),jeopardy.show_number.max())


# q = lambda row: jeopardy.question for row in jeopardy.show_number if jeopardy.show_number == x)

rndm_int = rd.randint(0,216929)

random_d_filter = jeopardy.iloc[rndm_int,1]
random_q_filter = jeopardy.iloc[rndm_int,5]
random_category_filter = jeopardy.iloc[rndm_int,3]

print('\n' + '\n' "Category: " + random_category_filter + '\n')
print( "Question ("+str(random_d_filter)+ "):  " + random_q_filter )
# answer_attempt = input('place answer here you nice person--->')
# filter answer
#     make everything lowercase(in the answer)
#     make the real answer lowercase
    #split real answer into a list. how do you do that?
    #splith thier answer ito a list. how do you do that?

    #us isin to test each word of the real answer.

#build function that tests filtered answer.
    #if true return "thats correct"
    #if fals return "no its 'real_answer'


print('\n' + "  WRONG   the answer is.... What/who is " + jeopardy.iloc[rndm_int,6])



# without give any parameters 
# print(x)







#tell them the categories and amounts
#ask them which category
#ask them for how much 
#choose the question they picked.
#print the questio they picked
#ask for the answer
#maybe timed for extra credit
#clean their answer
#check their answer against real answer
#if they are the same tell them the got it right.


# show_number


