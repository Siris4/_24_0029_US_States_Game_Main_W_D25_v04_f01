
import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")

# turtle.shape("square")
image = "blank_states_img.gif"   #you can load in a new image as a new shape
screen.addshape(image)

counter_correct_answer = 0
turtle.shape(image)   # available to be used by turtle. instead of using "circle" or "square" we can place image here, to display it!

total_guessed_states_so_far = []

while len(total_guessed_states_so_far) < 50:
    user_state_answer = screen.textinput(title=f"{len(total_guessed_states_so_far)}/50 States Correct", prompt="Guess a State: ").title()
    # user_answer_in_title_case = user_state_answer.title()     # this has been moved to the line above, attached to the very end.

# TODO: capitilized letters will not matter. Code it to be that way
# Checks against correct answer in the 50_states.csv. reading from CSV data. Place the name in that exact location.
# Correct answer? Count and make it 4/50

    dataframe = pandas.read_csv("50_states.csv")
# print(data)  #this prints the entire 50 x 3 DataFrame
    all_states_list = dataframe["state"].to_list()    # print(all_states_list)  prints out the whole list of JUST the 50 states, not the coords.
                        #or dataframe.state.to_list()  (gets a data Series, and we want to convert it into a List)

# Iterate over each row in the DataFrame
    if user_state_answer == "Exit":
        missing_states = []                     # TODO take the guessed states, compare them to all states, and then create a new list of all the missing states.
        for state in all_states_list:
            if state not in total_guessed_states_so_far:
                missing_states.append(state)
        new_data_missing_states = pandas.DataFrame(missing_states)
        new_data_missing_states.to_csv("states_to_learn")
        # print(missing_states)
        break
# "If the user's answer is one of the states in all of the states of the 50_states.csv then..." psuedo-code: and if they got it right, Create a turtle to write the name of the state at the state's x and y coord:
    if user_state_answer in all_states_list:
        total_guessed_states_so_far.append(user_state_answer)  # ORRR: counter_correct_answer += 1
        toby = turtle.Turtle()
        print(user_state_answer)
        toby.hideturtle()
        toby.penup()
        state_data = dataframe[dataframe.state == user_state_answer]  #this is going to get/pull out the row where the state equals the answer_state. then save the whole thing as "state_data" variable.
        toby.goto(int(state_data.x), int(state_data.y))
        toby.write(user_state_answer)    # not this: (state_data.state) cuz you get extra chars from it being extracted from the Series format. !!!! (state_data.state.item()) is what you want!!!!
        #reloops the while loop, as long as it's less than 50 states guessed so far

# screen.exitonclick()  #don't need this, since we have a break if "exit" gets typed


