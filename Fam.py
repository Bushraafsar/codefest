#Task 2:
#You have got chikens(2 legs), cows(4 legs) and pig(4 legs) on your farm retun the total no of legs on your farm.
chickens = int(input("Enter no. of chickens in the farm: "))
cows = int(input("Enter no. of cows in the farm: "))
pigs = int(input("Enter no. of pig in the farm: "))
def total_legs(chickens,cows,pigs):
    chickens_legs = chickens*2
    cows_legs = cows*4
    pigs_legs = pigs*4
    total = chickens_legs+cows_legs+pigs_legs
    return total
print(total_legs(chickens,cows,pigs))    