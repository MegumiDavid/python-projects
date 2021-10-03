from replit import clear
from art import logo

print(logo)

keep_going = True
auction = {}
while keep_going == True:
  name = input("What's your name? \t")
  bid = float(input("What's your bid? \t$"))
  auction[name] = bid

  option = input("New bid? [yes] or [no]\t").lower()

  if option == 'yes':
    clear()
  else:
    keep_going = False

biggest_bid = 0
for key in auction:
  if auction[key] >= biggest_bid:
    biggest_bid_name = key
    biggest_bid = auction[key]

print(f"The winner is {biggest_bid_name} with a bid of ${biggest_bid}")
