import time
import turtle
from turtle import Turtle, Screen
import pandas as pd
FONT = 'monaco', 10, "bold"
data = pd.read_csv('/Users/akashsingh/Desktop/100Days Python/day-25-us-states-game-start/50_states.csv')
screen = Screen()
screen.title("U.S. States Game")
image = "/Users/akashsingh/Desktop/100Days Python/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
tim=Turtle()
timmy=Turtle()
timmy.shape(image)
tim.penup()
tim.hideturtle()
gussed_state=[]


all_state=data.state.to_list()
missing_state=[]
while len(gussed_state)<50:
    answer_state = screen.textinput(title=f"{len(gussed_state)}/50 States Correct", prompt="What's another state's name").title()
    if answer_state.lower()=='exit':
        # for state in all_state:
        #     if state not in gussed_state:
        #         missing_state.append(state)
        missing_state=[state for state in all_state if state not in gussed_state ]
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv('/Users/akashsingh/Desktop/100Days Python/day-25-us-states-game-start/not_guessed_state.csv')
        break
    state_data = data[data['state'] == answer_state]
    if answer_state in all_state:
        state_name = state_data['state']
        # state_x = int(state_data['x'])
        # state_y = int(state_data['y'])
        gussed_state.append(answer_state)
        tim.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        tim.write(f"{state_data.state.item()}", move=False, align='left', font=FONT)
screen.bye()
# state_dict={
#     # 'Guessed state':gussed_state,
#     'Not Guessed state':missing_state
#
# }
# data_frame=pd.DataFrame(state_dict)
# data_frame.to_csv('/Users/akashsingh/Desktop/100Days Python/day-25-us-states-game-start/not_oguessed_state.csv')
# print(data_frame)

