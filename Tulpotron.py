from time import sleep
import requests

print(" __   Welcome to Tulpotron")
print("/  \  Version Crystal 0.1")
print("\__/  ©2019 Sankti")
print(" ")

declaration = input("Would you like to speak to Tulpotron? ")

if declaration in ["No", "no", "N", "n"]:
  print("Understood. Terminating process...")

  sleep(3)

  quit()

elif declaration in ["Yes", "yes", "Y", "y"]:
  print("Welcome. My name is Tulpotron.")

else:
 print("Invalid input. Terminating process...")

 sleep(3)

 quit()

user_name = input("Who are you? ")

print("Hello,", user_name + ".")

sleep(1)

user_temperature = input("Tell me, what is the temperature in the place you are now in? Please type a value in degrees Celsius. ")

#"It's easier to ask forgiveness than permission."
try:
  int(user_temperature)
except NameError and ValueError:
  print("I will only accept an answer in integers (degrees Celsius). Terminating process...")

  sleep(3)

  quit()

print("Understood. Your current environment's temperature is", user_temperature + "°C.")

sleep(2)

if int(user_temperature) >= 100:
  print("You must be boiling!")
elif int(user_temperature) > 14:
  print("That's rather hot.")
elif int(user_temperature) > 0:
  print("That's not too bad.")
elif int(user_temperature) < -273.15:
  print("Don't try to fool me!")
else:
  print("That's freezing cold!")

sleep(2)

user_country = input("Could you please tell me the name of the country you're currently in? ")

print("Thank you. Processing...")

country_req = "https://restcountries.eu/rest/v2/name/" + user_country + "?fullText=true"

country_data = requests.get(country_req).json()

sleep(2)

try:
  print(user_country + ", that's interesting. I've always wanted to visit", country_data[0]["capital"] + ".")
except KeyError:
  print("I'm sorry, I did not find", user_country, "in my database. Terminating process...")

  sleep(3)

  quit()

sleep(2)

visit_answer = input("Have you ever ben there? ")

sleep(2)

if visit_answer in ["No", "no", "N", "n"]:
  print("That's unfortunate. I hope one day you'll get to go there. I've heard it's one of the greatest cities in", country_data[0]["subregion"] + ".")

elif visit_answer in ["Yes", "yes", "Y", "y"]:
  print("That's great! You have to tell me about it one day! I've heard it's one of the greatest cities in", country_data[0]["subregion"] + ".")

else:
 print("Invalid input. Terminating process...")

 sleep(3)

 quit()

sleep(5)

print("Well,", user_name + ", it was fun to meet one of the", country_data[0]["population"], "people living in", user_country + ". I hope you have a great day!")

sleep(3)

quit()
