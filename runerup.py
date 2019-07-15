#Task 4:
#You are given a scores store them in a list and find the score of runner up:
list_score = []
for i in range(5):
  score = int(input("Enter scores :"))
  list_score.append(score)
list_score.sort()
print(list_score)
print("The score of runner up is: ",list_score[len(list_score)-2])

