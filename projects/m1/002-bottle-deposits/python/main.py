#calculate containers

small_containers=0.10 #small containers by users input
big_containers=0.25 #big containers by users input

containers_little=input("How many containers do you have below 1 litres?: ")
price_small_containers= int(containers_little)*(small_containers)

containers_big=input("How many containers do you have more than 1 litres?: ")
price_big_containers= int(containers_big)*(big_containers)

#calculare refudn total for users
refund_total=float(price_small_containers)+float(price_big_containers)

print("Your refund is",refund_total,"$")