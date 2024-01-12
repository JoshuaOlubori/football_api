import random
from datetime import datetime

# Define the greetings lists
good_morning_greetings = [
    "Top of the morning to you, Mr. Akindele!",
    "Good morning, Mr. Akindele! Wishing you a wonderful day ahead.",
    "Rise and shine, Mr. Akindele!",
    "Morning, Mr. Akindele!",
    "Greetings, Mr. Akindele!",
    "Hello, Mr. Akindele! Wishing you a bright and cheerful morning.",
    "A pleasant good morning, Mr. Akindele!",
    "Hello there, Mr. Akindele!",
    "Good day, Mr. Akindele!"
]

good_afternoon_greetings = [
    "Good afternoon, Mr. Akindele! I trust your day is going well.",
    "Hello, Mr. Akindele!",
    "Afternoon, Mr. Akindele!",
    "Greetings, Mr. Akindele!",
    "Mr. Akindele, good day to you!",
    "Hello there, Mr. Akindele! Good afternoon."
]

good_evening_greetings = [
    "Good evening, Mr. Akindele! I hope you had a wonderful day.",
    "Evening, Mr. Akindele!",
    "Hello, Mr. Akindele!",
    "Mr. Akindele, good night!",
    "Good evening, Mr. Akindele!"
]

# Get the current time
current_time = datetime.now().time()

# Function to get the appropriate greeting based on the time of the day
def get_greeting():
    if current_time < datetime.strptime("12:00", "%H:%M").time():
        print(random.choice(good_morning_greetings))
    elif current_time < datetime.strptime("17:00", "%H:%M").time():
        print(random.choice(good_afternoon_greetings))
    else:
        print(random.choice(good_evening_greetings))
