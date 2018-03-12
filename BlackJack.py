import random
class User:
	def __init__(self,balance,name,hand=[],total=0):
		self.balance=balance
		self.name=name
		self.total=0
		self.hand=[]
	
	def get_balance(self):
		return self.balance
	def balance_calc(self,deal,win_type):
		self.balance=int(self.balance+win_type*deal)
		return self.balance
	def total_calc(self,card):
		self.total+=card
		return self.total
	def get_total(self):
		return self.total

suit=["Heart","Diamond","Spade","Club"]
card=["King","Queen","Jack","A","2","3","4","5","6","7","8","9","10"]
def card_choose(hand):
	suit=random.randint(0,3)
	card=random.randint(0,12)
	while (suit,card) in hand:
		suit=random.randint(0,3)
		card=random.randint(0,12)
	return (suit,card)
def get_score(card):
	if card in [0,1,2]:
		return 10
	elif card==3:
		return 11
	else:
		return card-2
def dealer_draw(call_no):
	global dealer_total
	suit_no,card_no=card_choose(dealer_hand)
	dealer_hand.append((suit_no,card_no))
	dealer_total+=get_score(dealer_hand[call_no-1][1])
def player_draw(call_no):
	suit_no,card_no=card_choose(player.hand)
	player.hand.append((suit_no,card_no))
	player.total+=get_score(player.hand[call_no-1][1])


print("!!!WELCOME TO THE GAME OF BLACKJACK!!!")
name=input("Please enter your name!!:  ")
player=User(3000,name)
hit_over=False
dealer_total=0
dealer_hand=[]
while True:
	if player.balance==0:
		print("You are out of balance-Start the game afresh!!!\n")
		break
	print("Balance=%d"%player.get_balance())
	while True:
		try:
			deal=int(input("How much do u wanna deal:    "))
		except:
			print("wrong kind of input-Enter a valid number\n")
			continue
		if deal not in range(1,player.get_balance()+1):
			print("Wrong Input!!! Enter proper deal amount\n")
			continue
		else:
			break
	suit_no,card_no=card_choose(dealer_hand)
	dealer_hand.append((suit_no,card_no))
	dealer_total+=get_score(card_no)
	print("DEALER CARD-1:%s,%s" %(suit[suit_no],card[card_no]))
	suit_no,card_no=card_choose(player.hand)
	player.hand.append((suit_no,card_no))
	player.total_calc(get_score(card_no))
	suit_no,card_no=card_choose(player.hand)
	player.hand.append((suit_no,card_no))
	player.total_calc(get_score(card_no))
	print("PLAYER CARD-1:%s,%s" %(suit[player.hand[0][0]],card[player.hand[0][1]]))
	print("PLAYER CARD-2:%s,%s" %(suit[player.hand[1][0]],card[player.hand[1][1]]))
	print("player total:%d" %(player.total))
	if(player.total==21):
		print("player BLACKJACK")
		(suit_no,card_no)=card_choose(dealer_hand)
		dealer_hand.append((suit_no,card_no))
		print("DEALER CARD-2:%s,%s" %(suit[suit_no],card[card_no]))
		dealer_total+=(get_score(dealer_hand[1][1]))
		if dealer_total==21:
			print("Dealer BLACKJACK")
			print("Push")
		else:
			player.balance_calc(deal,1.5)
			posn_1=0
			posn=0
			call_no=2
			while dealer_total<17:
				call_no+=1
				dealer_draw(call_no)
				print("DEALER CARD-%d:%s,%s"%(call_no,suit[dealer_hand[call_no-1][0]],card[dealer_hand[call_no-1][1]]))
				if dealer_total>21:
					for suit_no,card_no in dealer_hand[posn:]:
						posn_1+=1
						if card_no==3:
							dealer_total-=10
							break
					posn=posn_1
			if dealer_total>21:
				print("dealer total=%d" %(dealer_total))
				print("Dealer Bust")
				print("you get %d" %(deal*2.5))
				print("Player Balance=%d" %player.balance)
			else:
				print("dealer total=%d" %(dealer_total))
				print("dealer lose")
				print("you get %d" %(deal*2.5))
				print("Player Balance=%d" %player.balance)
	else:
		if (deal*2)<=player.balance:
			option=(input("Enter choice:\n1 for double down\n2 for hit\n3 for stand\n"))
			while option not in ['1','2','3']:
				option=(input("Wrong choice...Enter again:   "))
		else:
			option=int(input("Enter choice:\n1 for hit\n2 for stand\n"))
			while option not in [1,2]:
				option=int(input("Wrong choice...Enter again:   "))
			option+=1
			option=str(option)
		if (option=='1'):
			suit_no,card_no=card_choose(player.hand)
			player.hand.append((suit_no,card_no))
			print("PLAYER CARD-3:%s,%s" %(suit[player.hand[2][0]],card[player.hand[2][1]]))
			player.total_calc(get_score(card_no))
			(suit_no,card_no)=card_choose(dealer_hand)
			dealer_hand.append((suit_no,card_no))
			print("DEALER CARD-2:%s,%s" %(suit[suit_no],card[card_no]))
			if player.total>21:
				for suit_no,card_no in player.hand:
					if card_no==3:
						player.total-=10
			dealer_total+=(get_score(dealer_hand[1][1]))
			if dealer_total==21:
				print("Dealer BLACKJACK")
				if player.total>21:
					print("player bust")
				else:
					print("player total:%d"%player.total)
				print("you lose:%d"%(deal*2))
				player.balance_calc(deal,-2)
				print("Player Balance=%d" %player.balance)
			else:
				if player.total>21:
					print("player bust")
					print("you lose:%d"%(deal*2))
					player.balance_calc(deal,-2)
					print("Player Balance=%d" %player.balance)
				else:
					print("player total=%d" %(player.total))
					posn_1=0
					posn=0
					call_no=2
					while dealer_total<17:
						call_no+=1
						dealer_draw(call_no)
						print("DEALER CARD-%d:%s,%s"%(call_no,suit[dealer_hand[call_no-1][0]],card[dealer_hand[call_no-1][1]]))
						if dealer_total>21:
							for suit_no,card_no in dealer_hand[posn:]:
								posn_1+=1
								if card_no==3:
									dealer_total-=10
									break
							posn=posn_1
					if dealer_total>21:
						print("dealer total=%d" %(dealer_total))
						print("Dealer Bust")
						print("you get %d" %(deal*4))
						player.balance_calc(deal,2)
						print("Player Balance=%d" %player.balance)
					else:
						print("dealer total=%d" %(dealer_total))
						if dealer_total>player.total:
							print("dealer win")
							print("you lose %d" %(deal*2))
							player.balance_calc(deal,-2)
						elif dealer_total==player.total:
							print("Push")
						else:
							print("dealer lose")
							print("you win %d" %(deal*4))
							player.balance_calc(deal,2)
						print("Player Balance=%d" %player.balance)
		if option=='2':
			call_no=2
			hit='1'
			hit_over=True
			last_posn=0
			while hit=='1':
				call_no+=1
				suit_no,card_no=card_choose(player.hand)
				player.hand.append((suit_no,card_no))
				print("PLAYER CARD-%d:%s,%s"%(call_no,suit[player.hand[call_no-1][0]],card[player.hand[call_no-1][1]]))
				player.total_calc(get_score(card_no))
				if player.total>21:
					for (suit_no,card_no) in player.hand[last_posn:]:
						if card_no==3:
							player.total-=10
					last_posn=call_no
				if player.total>21:
					print("player bust")
					(suit_no,card_no)=card_choose(dealer_hand)
					dealer_hand.append((suit_no,card_no))
					print("DEALER CARD-2:%s,%s" %(suit[suit_no],card[card_no]))
					print("dealer win")
					print("you lose %d" %(deal))
					player.balance_calc(deal,-1)
					print("Player Balance=%d" %player.balance)
					hit_over=False
					break
				print("player total=%d"%player.total)
				hit=(input("Do u want to:\n1 for hit again or\n 2 for stand??\n"))
				while hit not in ['1','2']:
					hit=(input("Wrong input...Enter again:   "))
		if hit_over==True or option=='3':
			posn_1=0
			posn=0
			call_no=1
			while dealer_total<17:
				call_no+=1
				dealer_draw(call_no)
				print("DEALER CARD-%d:%s,%s"%(call_no,suit[dealer_hand[call_no-1][0]],card[dealer_hand[call_no-1][1]]))
				if call_no==2:
					if dealer_total==21:
						break

				if dealer_total>21:
					for suit_no,card_no in dealer_hand[posn:]:
						posn_1+=1
						if card_no==3:
							dealer_total-=10
					posn=posn_1
			if dealer_total>21:
				print("dealer total=%d" %(dealer_total))
				print("Dealer Bust")
				print("you get %d" %(deal*2))
				player.balance_calc(deal,1)
				print("Player Balance=%d" %player.balance)
			else:
				print("dealer total=%d" %(dealer_total))
				if dealer_total==21 and call_no==2:
					print("Dealer BLACKJACK")
				if dealer_total>player.total:
					print("dealer win")
					print("you lose %d" %(deal))
					player.balance_calc(deal,-1)
				elif dealer_total==player.total:
					print("Push")
				else:
					print("dealer lose")
					print("you win %d" %(deal*2))
					player.balance_calc(deal,1)
				print("Player Balance=%d" %player.balance)
	interest=input("Do you want to deal again-Yes or no").lower()
	while interest not in ["yes","no"]:
		interest=input("Enter again-Yes or no!!").lower()
	if interest=="no":
		break
	else:
		dealer_total=0
		player.total=0
		player.hand=[]
		dealer_hand=[]
		continue
print("Good Bye %s"%player.name)







