#This program shows what time it is in the village based on the user's clock.
from datetime import datetime

current_hour = datetime.today().hour

night = [0, 1, 2, 3, 4, 5]
morning = [6, 7, 8, 9, 10, 11]
afternoon = [12, 13, 14, 15, 16, 17]
evening = [18, 19, 20, 21, 22, 23]

if current_hour in night:
    print("It is now a cold night in the village.")
if current_hour in morning:
    print("It is now a cloudy morning in the village")
if current_hour in afternoon:
    print("It is now a rainy afternoon in the village.")
if current_hour in evening:
    print("It is now a beautiful evening in the village.")
