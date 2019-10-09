import sys, time

# Define the scrolltext functions
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_quick(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def intro_text():
    print_slow("A long, long time ago..." + "\n\n")
    print_slow("..." + "\n\n")
    print_slow("(OK, on Monday 7th October at around 2 o'clock in the afternoon.)" + "\n\n")
    print_slow("..." + "\n\n")
    print_slow("In a galaxy far, far away..." + "\n\n")
    print_slow("..." + "\n\n")
    print_slow("(OK, in the Contino Liverpool Street office, meeting room 3.)" + "\n\n")
    print_slow("..." + "\n\n")
    print_quick("A brave and noble warrior (OK, just me)...made a promise to the PeopleOps team.\n" +
    "That promise? That he would produce (in Python) a story of noble deeds.\n" + 
    "A story foretelling a battle against the combined forces of the mighty Cloud Certifications.\n\n")
    print_slow("..." + "\n\n" + "..." + "\n\n")
    print_slow("This is that story....\n\n" + "..." + "\n\n" + "..." + "\n\n")
    time.sleep(3)

def filler_space():
    print_slow("..." + "\n\n" + "..." + "\n\n" + "..." + "\n\n")