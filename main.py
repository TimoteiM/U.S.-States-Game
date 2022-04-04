import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
game_over = False
attempts = 50
while not game_over:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
    else:
        attempts -= 1
    if attempts == 0:
        game_over = True
        screen.title("You lose!")
to_learn = []
for state in all_states:
    if state not in guessed_states:
        to_learn.append(state)

new_data = pandas.DataFrame(to_learn)
new_data.to_csv("states_to_learn.csv")


print(to_learn)





