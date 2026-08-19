import pandas
import turtle

# screen setup
font = ('Arial', 8, 'bold')
screen = turtle.Screen()
screen.title("U.S State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv") # reads the csv states file
list_of_states = data["state"].tolist() # turns it into a list


# states correct scoreboard and game is active loop
states_correct = 0
game_is_active = True;


# game is active loop
while game_is_active:
    # user guess
    user_guess = screen.textinput(title=f"Guess the state {states_correct} / 50", prompt="Enter a state name?")
    # if guess all states game ends
    if states_correct == 50:
        game_is_active = False
    # loops through list we made to find out if state guess was correct and lowers both user and state
    for states in list_of_states:
        if user_guess.lower() == states.lower():
            num = list_of_states.index(states) # gets the number of state in list using index
            x = data.iloc[num]["x"] # gets x cord of state using the num variable above
            y = data.iloc[num]["y"] # gets y cord of state using the num variable above
            states = turtle.Turtle()  # creates a state turtle
            states.hideturtle() # hides the turtle shape
            states.penup() # lifts pen up
            states.goto(x,y) # goes to state location based on x v from csv
            states.write(list_of_states[num],font=font) # writes state name from list
            states_correct += 1 # adds to state guessed correct list


screen.mainloop()
