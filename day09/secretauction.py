# Secret Auction
import art
import os

print(art.logo)
print("\nWelcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    # Try Again
    tryagain = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if(tryagain != "yes"):
        bidding_finished = True
    # Clear Console
    os.system("cls")


# Check highest bid
highestbid = max(bids)
print(f"The winner is {highestbid} with a bid of ${bids[highestbid]}")
