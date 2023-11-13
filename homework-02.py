# Radhika Rukmangadhan 
# November 5
# Homework 2

user = input("Hello! What is your name?")
birth_year = int(input("Enter your year of birth: "))
current_year = 2023

while birth_year>current_year: #Ques 10
    birth_year = int(input("Please provide valid year: "))

user_age = current_year-birth_year
print("You are", user_age , " years old.") #Ques 1
human_heartbeat = user_age*70*60*24*30*12 #assuming 70 beats a minute
print( user, ", your heart has beaten", human_heartbeat, " times in your life.") #Ques2
whale_heartbeat = user_age*2*60*24*30*12 #assuming 2 beats per minute #Ques 3
print ("If you were a whale, you heart would have beaten", whale_heartbeat, "times till now.")
rabbit_heartbeat = user_age*160*60*24*30*12 #assuming 160 beats per minute #Ques 4a
if rabbit_heartbeat>=1000000000: #Ques 4b
    rabbit_new_heartbeat = rabbit_heartbeat/1000000000
    print ("If you were a rabbit, your heart would have beaten", rabbit_new_heartbeat," billion times till now.")
else: print("If you were a rabbit, your heart would have beaten", rabbit_heartbeat, "times till now.")
if rabbit_heartbeat>=1000000000: #Ques 5
    rabbit_new_heartbeat = rabbit_heartbeat/1000000000
    print ("If you were a rabbit, your heart would have beaten", round(rabbit_new_heartbeat)," billion times till now.") 
else: print("If you were a rabbit, your heart would have beaten", rabbit_heartbeat, "times till now.")
age_difference=user_age-32
if age_difference == 0: #Ques 6a
    print("You are the same age as me!")
elif age_difference > 0:
    print("You are", age_difference," years older than me.")
else:
    print("You are", abs(age_difference)," years younger than me.")
if birth_year%2 == 0: #Ques 6b
    print("You were born in an even year")
else:
    print("You were born in an odd year")
democratic_president_years = [1980, 1993, 2009, 2021] #Ques 7
if birth_year<1980:
    print("No president for you, sorry")
else:
    count = 0
    for year in democratic_president_years:
        if year >= birth_year:
            count += 1
    if birth_year > 2021:
        count = 1
    print("There was a Democratic president in office", count, "times since your birth year.")

us_presidents_since_1980 = {  #Ques 8
    "1980": "Jimmy Carter",
    "1981": "Ronald Reagan",
    "1989": "George H.W. Bush",
     "1993": "Bill Clinton",
     "2001": "George W. Bush",
     "2009": "Barack Obama",
     "2017": "Donald Trump",
     "2021": "Joe Biden"
}

for year, president in us_presidents_since_1980.items():
    if birth_year >= int(year):
        match = president

print(match, " was in office when you were born.")

#Ques 9: The following was my previous attempt at Ques 8. I was trying to use two pointers to find the match in the tuple but I was not getting the correct results. I changed the tuple to a dictionary in my final answer to ques 8 and used if to match.
# us_presidents_since_1980 = [          
#     (1980, "Jimmy Carter"),
#     (1981, "Ronald Reagan"),
#     (1989, "George H.W. Bush"),
#     (1993, "Bill Clinton"),
#     (2001, "George W. Bush"),
#     (2009, "Barack Obama"),
#     (2017, "Donald Trump"),
#     (2021, "Joe Biden"),]
# for year1, president1 in us_presidents_since_1980:
#     for year2, president2 in us_presidents_since_1980:
#         print (f"{year1}, {year2}") 
#         if year1 <= birth_year and birth_year < year2:
#             print (f"{president1} was president when you were born")
#             break
#        # else:
#        #     continue
#   #  continuek

            