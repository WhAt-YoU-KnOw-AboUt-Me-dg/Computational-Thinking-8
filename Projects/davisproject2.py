party_points = 0
home_points = 0


answer = input("On a weekend would you rather A) go to a party, or B) stay home")
if answer == "A":
    party_points += 1
elif answer == "B":
    home_points += 1


answer = input( "Would you rather A) go to a dance party, or B) watch a movie at home?")
if answer == "A":
    party_points += 1
elif answer == "B":
    home_points += 1


answer = input("would you rather hang with your friends at A) party, or B) at your house.")
if answer == "A":
    party_points += 1
elif answer == "B":
    home_points += 1


answer = input ("would you rather A) go out to eat for fun or) B have a fun dinner at home?")
if answer == "A":
    party_points += 1
elif answer == "B":
    home_points += 1


answer = input ("do you like A) going to party's or) B staying home with parents")   
if answer == "A":
    party_points += 1
elif answer == "B":
    home_points += 1


answer = input ("do you like A) Loud music or) B music through headphones")
if answer == "A":
    party_points += 1
elif answer == "B":
    home_points += 1


# end of quiz:
if party_points > home_points:
    print ("you are the life of the party")
elif home_points > party_points:
    print ("you are a stay at home person")