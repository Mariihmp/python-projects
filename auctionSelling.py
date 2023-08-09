

print('''
     _____>>>>
    /     \>>>>
   /_     _\>>>>
     |   |
     |   |
     |   |
     |___|
     |___|
     WELCOME TO THE BETTIN CONTEST\n ''')
bids = {}
biding_finsished = False

def find_highest_bidder(bidding_record):
    price_rec_li = []
    for vals in bidding_record.values():
        price_rec_li.append(vals)
    for price in price_rec_li:
        if price>price_rec_li[0]:
            print(f"the highset bet is {price}")
        
        
    

while not biding_finsished:
    name = input("what's your name\n")
    price = input("what's your price\n")
    bids[name] = price
    should_continue = input("are there any other bidders? type Y or N \n")
    if should_continue.lower() == "n":
        find_highest_bidder(bids)
        biding_finsished = True
    elif should_continue == 'y':
        pass
            


    