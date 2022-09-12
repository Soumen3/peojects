'''Problem Statement: You have to write a Word Puzzle Game in which the user has to form the correct word out of a given set of characters. 
In the game the user has to solve this puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user in random 
sequence. Give the user score +1 for each correct answer and give -1 for each wrong answer. At last print the final score. You can store any 
number of words in the list, but in each round of the game only 5 words are shown to the user.'''



from random import*
words=['Father', 'Mother', 'Computer', 'Mouse', 'Display', 'Window', 'History', 'Language', 'Number', 'Bottle', 'Python', 'System']
problem=['TERHAF','HOTRME','PTCMORUE','EUSOM','PADSYIL','WWDION','TSOHIYR','LAGGUAEN','MERBUN','TTOBEL','HTOYNP','EMTYSS']
score=0
for i in range(5):
    print('Arrange the letters to form a valid word:')
    problem_word=choice(problem)
    print(problem_word)
    user=input('\n')
    indx=problem.index(problem_word)

    if user.upper()==words[indx].upper():
        score+=1
        print('\nCorrect\n')
    else:
        score-=1
        print('\nWrong\n')

print('\nYour net score is:',score)

