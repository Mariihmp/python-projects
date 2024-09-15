
import turtle
import pandas as pd
weather_infor = pd.read_csv('weather.csv')
#
#
# max_val= weather_infor['temp'].max()
# condition = weather_infor['condition'].tolist()
# row = weather_infor[weather_infor.temp ==max_val]
# print(row)#this returns the row that has the biggest temp
#
# data_dict = {
#     "students": ["amy","james",'angela'],
#     "scores":[12,14,17]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

scr = turtle.Screen()
scr.title('US STATES GAMES')

image = "blank_states_img.gif"
scr.addshape(image)
turtle.shape(image)
#get the x and y values from csv int a tuple (x,y)
#ask the user for name of the state -- the key is
#name of the state and the value is the (x,y)
#if user types the state correctly the name of the
#state is goes to its values

states =pd.read_csv('50_states.csv')
#keys are state x y
# print(states['state

state = states['state']
x_cor = states['x']
y_cor = states['y']
guessed_state = []
missing_states = []


while len(guessed_state)<50:
    answer_state = scr.textinput(title=f'{len(guessed_state)/50} correct state', prompt="WHAT'S ANOTHER STATE'S NAME?")

    if answer_state.title() in state.tolist():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data['x']),int(state_data['y']))
        t.write(state_data.state.item())




scr.exitonclick()