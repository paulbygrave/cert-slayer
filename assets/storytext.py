import sys, time

# Define the scrolltext functions
def print_quick(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def intro_text():
    print_quick("\n\n\nA long, long time ago...\n\n" +
    "...\n\n" +
    "(OK, on Monday 7th October at around 2 o'clock in the afternoon.)\n\n" +
    "...\n\n" +
    "In a galaxy far, far away...\n\n" +
    "...\n\n" +
    "(OK, in the Contino Liverpool Street office, meeting room 3.)\n\n" +
    "...\n\n" +
    "A brave and noble warrior (yeah, who am i kidding?!)...made a promise to the PeopleOps team.\n" +
    "That promise? That he would produce (in Python) a story of noble deeds.\n" + 
    "A story foretelling one hero's struggle against the combined forces of the mighty Cloud Certifications.\n\n" +
    "..." + "\n\n" + "..." + "\n\n" +
    "This is that hero's story....\n\n" + "..." + "\n\n" + "..." + "\n\n")
    time.sleep(2)

def fillspace():
    print_quick("..." + "\n\n" + "..." + "\n\n" + "..." + "\n\n")

def quest_text():
    print_quick("\n\nOur hero is new to Contino.\n" +
    "...\n" + 
    "They have completed the onboarding, setup their new equipment and have decided to upskill!\n" +
    "...\n" + 
    "They start to look for something to study...\n" +
    "...\n" + 
    "Oh no! It's an ambush!\n")
    time.sleep(1)

def epilogue_text():
    print_quick("\n\nAnd so ends the tale of our hero.\n" +
    "\n" + 
    "Whether they triumphed over adversity or succumbed to the enemy, I hope you had fun playing!\n" +
    "\n" + 
    "I hope that this program has taught you a little about the power of Python!\n" +
    "\n" + 
    "Untill next time...\n")
    time.sleep(1)

def end_credits():
    print_slow("\nCredits\n\n" + 
    "Studio:\n" +
    "Designer: Paul\n" +
    "Story: Paul\n" + 
    "Lead Programmer: Paul\n\n" +
    "QA:\n" +
    "Alpha Tester: Paul\n" + 
    "Beta Tester: Sean\n\n" + 
    "Special Thanks:\n" +
    "Kostas\n\n\n")
    time.sleep(1)
