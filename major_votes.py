# Task 7
# Create a function that returns the majority vote.A majority vote is an elemment that occirs > n/2 timesin alist:
print(" there are 4 teams who participate in this event!")
print("A","B","C","D") 
from collections import Counter
def major_votes():
    votes = []
    for i in range(1,6):
        vote = input("Cast your vote to the favourite team:")
        votes.append(vote)
    print(votes)
    N = len(votes)
    votes = Counter(votes) # using counter function to count the apperance of each character
    for i,j in votes.items():
        if j > (N/2):
            winner_team = i 
            print("Team",i,"gets the majority of votes")
        else:
            print("--None--")    
major_votes()            
