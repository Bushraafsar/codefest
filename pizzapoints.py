# Task 09
# Python program that create afunction that takes a dictionary of customers,a min order & min price and return a list off customers that are eligible for a free pizza:
# TO EARN FREE PIZZA CUSTOMERS SHOULD ORDER MINIMUM 3 PIZZAS OF MINIMUM 200 RUPEES.
min_order = 3
min_price = 200
customer_dic = {
    "amna":[500,200,150,270,150,100,],
    "iqbal":[200,150,50,200,150,400],
    "imran":[200.350,50,100],
    "sameer":[120,100,20,10],
}
winner_list =[]
def free_pizza(customer_dic,min_order,min_price,counter = 0):
    for i,j in customer_dic.items():
        for j in customer_dic[i]:
            if j >= min_price:
                counter += 1   
        if counter >= min_order:
            winner = i
            winner_list.append(winner)
            counter = 0
    print("the list of customers who get free pizza from pizza point is :", winner_list)
    
                
    
free_pizza(customer_dic,min_order,min_price)              