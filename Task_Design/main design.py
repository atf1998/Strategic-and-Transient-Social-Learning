from psychopy import visual, event, data, core
import random
import pandas as pd
import csv


img1_path = 'D:/University/MSc/Thesis/task/Images/1.png'
img2_path = 'D:/University/MSc/Thesis/task/Images/2.png'
img3_path = 'D:/University/MSc/Thesis/task/Images/3.png'
img4_path = 'D:/University/MSc/Thesis/task/Images/4.png'
img5_path = 'D:/University/MSc/Thesis/task/Images/5.png'
img6_path = 'D:/University/MSc/Thesis/task/Images/6.png'
img7_path = 'D:/University/MSc/Thesis/task/Images/7.png'
img8_path = 'D:/University/MSc/Thesis/task/Images/8.png'
img9_path = 'D:/University/MSc/Thesis/task/Images/9.png'

b_trial = [15, 45, 105]     # Task
# b_trial = [6, 12, 18]    # training

subject_id = '31'
group = 1

if group == 1:
    path = 'D:/University/MSc/Thesis/task/data/trained/4 arm/'
else:
    path = 'D:/University/MSc/Thesis/task/data/not trained/4 arm/'

win = visual.Window([1707, 1067], color="Black", fullscr=True)
# win = visual.Window([800, 600], color="Black", fullscr=False)
reaction_clock = core.Clock()

cards = [visual.Rect(win, width=0.3, height=0.8, pos=[-0.75, 0], lineWidth=5, fillColor='grey'),
         visual.Rect(win, width=0.3, height=0.8, pos=[-0.25, 0], lineWidth=5, fillColor='grey'),
         visual.Rect(win, width=0.3, height=0.8, pos=[0.25, 0], lineWidth=5, fillColor='grey'),
         visual.Rect(win, width=0.3, height=0.8, pos=[0.75, 0], lineWidth=5, fillColor='grey')]


social_cards = [visual.Rect(win, width=0.3, height=0.8, pos=[-0.75, 0], lineColor='BlueViolet'),
                visual.Rect(win, width=0.3, height=0.8, pos=[-0.25, 0], lineColor='BlueViolet'),
                visual.Rect(win, width=0.3, height=0.8, pos=[0.25, 0], lineColor='BlueViolet'),
                visual.Rect(win, width=0.3, height=0.8, pos=[0.75, 0], lineColor='BlueViolet')]

agent_names = [visual.TextStim(win, text='A', pos=[-0.5, 0]),
               visual.TextStim(win, text='B', pos=[-0.3, 0]),
               visual.TextStim(win, text='C', pos=[-0.1, 0]),
               visual.TextStim(win, text='NO AGENT', pos=[0.3, 0])]

agent_A_shape = [visual.ShapeStim(win, vertices=[[-0.04, -0.04], [0.04, -0.04], [0, 0.04]],pos=cards[0].pos + [-0.1, 0] , fillColor='grey', lineColor='black'),
                 visual.ShapeStim(win, vertices=[[-0.04, -0.04], [0.04, -0.04], [0, 0.04]],pos=cards[1].pos + [-0.1, 0] , fillColor='grey', lineColor='black'),
                 visual.ShapeStim(win, vertices=[[-0.04, -0.04], [0.04, -0.04], [0, 0.04]],pos=cards[2].pos + [-0.1, 0] , fillColor='grey', lineColor='black'),
                 visual.ShapeStim(win, vertices=[[-0.04, -0.04], [0.04, -0.04], [0, 0.04]],pos=cards[3].pos + [-0.1, 0] , fillColor='grey', lineColor='black')]

agent_B_shape = [visual.Rect(win, width=0.08, height=0.08, pos=cards[0].pos + [0, 0], fillColor='grey', lineColor='black'),
                 visual.Rect(win, width=0.08, height=0.08, pos=cards[1].pos + [0, 0], fillColor='grey', lineColor='black'),
                 visual.Rect(win, width=0.08, height=0.08, pos=cards[2].pos + [0, 0], fillColor='grey', lineColor='black'),
                 visual.Rect(win, width=0.08, height=0.08, pos=cards[3].pos + [0, 0], fillColor='grey', lineColor='black')]

agent_C_shape = [visual.Circle(win, radius=0.04, pos = cards[0].pos +[0.1, 0], fillColor='grey', lineColor='black'), 
                 visual.Circle(win, radius=0.04, pos = cards[1].pos +[0.1, 0], fillColor='grey', lineColor='black'),
                 visual.Circle(win, radius=0.04, pos = cards[2].pos +[0.1, 0], fillColor='grey', lineColor='black'),
                 visual.Circle(win, radius=0.04, pos = cards[3].pos +[0.1, 0], fillColor='grey', lineColor='black')]

agent_shapes = [visual.ShapeStim(win, vertices=[[-0.04, -0.04], [0.04, -0.04], [0, 0.04]],pos=[-0.5, 0] , fillColor='grey', lineColor=None),
                visual.Rect(win, width=0.08, height=0.08, pos=[-0.3, 0], fillColor='grey', lineColor=None),
                visual.Circle(win, radius=0.04, pos = [-0.1, 0], fillColor='grey', lineColor=None),
                visual.TextStim(win, text='NO AGENT', pos=[0.3, 0])]

red_cross = visual.ImageStim(
    win=win,
    image="D:/University/MSc/Thesis/task/Images/c2.png",
    size=0.17
)

coin = visual.ImageStim(
    win=win,
    image="D:/University/MSc/Thesis/task/Images/coin.png",
    size=0.2
)

results = []

################################################################################################################################################################################################
#                                                                                        FUNCTIONS
################################################################################################################################################################################################
def get_participant_choice():
    message = visual.TextStim(win, text='Please Make a choice.', pos=(0, 0.6))
    message.draw()
    for card in cards:
        card.draw()
    win.flip()
    reaction_clock.reset()
    choice = None
    conf = None
    while choice not in ['a', 's', 'd', 'f']:
        keys = event.waitKeys(timeStamped=reaction_clock)
        if keys:
            choice, choice_rt  = keys[0]
    message = visual.TextStim(win, text='Press 1,2,3,4 or 5 as your confidence.', pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    while conf not in ['1', '2', '3', '4', '5']:
        conf_keys = event.waitKeys(timeStamped=reaction_clock)
        if conf_keys:
            conf, conf_rt = conf_keys[0]
    if choice == 'a':
        choice_idx = 0
    elif choice == 's':
        choice_idx = 1
    elif choice == 'd':
        choice_idx = 2
    else:
        choice_idx = 3 
        
    return choice_idx, choice_rt, conf, conf_rt

def e_greedy(epsilon, idx):
    if random.random() > epsilon:
        return random.choice([0, 1, 2, 3])
    else:
        return idx
def e_second_greedy(epsilon, idx):
    if random.random() > epsilon:
        return random.choice([0, 1, 2, 3])
    else:
        return idx


def show_agents_choices(agent_A_choice, agent_B_choice, agent_C_choice, color):
    
    win.flip()
    # cards[agent_A_choice]
    # agent_A_text = visual.TextStim(win, text='A', pos=cards[agent_A_choice].pos + [0, 0.1], color='black')
    # agent_B_text = visual.TextStim(win, text='B', pos=cards[agent_B_choice].pos + [0, 0], color='black')
    # agent_C_text = visual.TextStim(win, text='C', pos=cards[agent_C_choice].pos + [0, -0.1], color='black')
    
    cards[agent_A_choice].setLineColor('BlueViolet')
    cards[agent_B_choice].setLineColor('BlueViolet')
    cards[agent_C_choice].setLineColor('BlueViolet')
    message = visual.TextStim(win, text='Press SPACE to continue', pos=(0, 0.55))
    for card in cards:
        card.draw()
    agent_A_shape[agent_A_choice].setFillColor('black')
    agent_B_shape[agent_B_choice].setFillColor('black')
    agent_C_shape[agent_C_choice].setFillColor('black')
    for idx in range(4):
        agent_A_shape[idx].draw()
        agent_B_shape[idx].draw()
        agent_C_shape[idx].draw()
    
    message.draw()
    win.flip()
    for card in cards:
        card.setFillColor(color)
        card.setLineColor(color)
    agent_A_shape[agent_A_choice].setFillColor('grey')
    agent_B_shape[agent_B_choice].setFillColor('grey')
    agent_C_shape[agent_C_choice].setFillColor('grey')
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    return sp_rt
    # core.wait(6.0)

def which_agent():
    output = ['A', 'B', 'C', 'ٔNo agent']
    message = visual.TextStim(win, text='Please choose between agents or choose non', pos=(0, 0.4))
    message.draw()
    for agent in agent_shapes:
        agent.draw()
    win.flip()
    reaction_clock.reset()
    choice = None
    while choice not in ['j', 'k', 'l', ';', 'semicolon', '59']:
        keys = event.waitKeys(timeStamped=reaction_clock)
        if keys:
            choice, choice_rt  = keys[0]
    
    if choice == 'j':
        ch_idx = 0
    elif choice == 'k':
        ch_idx = 1
    elif choice == 'l':
        ch_idx = 2
    else:
        ch_idx = 3
            
            
    return output[ch_idx], ch_idx , choice_rt

def show_chosen_agent(agent, choice, color):
    shape_idx = 0
    if agent == 'A':
        shape_idx = 0
    elif agent == 'B':
        shape_idx = 1
    else:
        shape_idx = 2
    chosen_shape = agent_shapes[shape_idx]
    last_pos = chosen_shape.pos
    chosen_shape.pos = cards[choice].pos + [0, 0]
    chosen_shape.setFillColor('black')
    message = visual.TextStim(win, text='Press SPACE to continue ', pos=(0, 0.55))
    cards[choice].setLineColor('BlueViolet')
    for card in cards:
        card.draw()
    chosen_shape.draw()
    message.draw()
    win.flip()
    for card in cards:
        card.setFillColor(color)
        card.setLineColor(color)
    chosen_shape.setFillColor('grey')
    chosen_shape.pos = last_pos
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    return sp_rt
    # core.wait(6.0)
################################################################################################################################################################################################
#                                                                                          START
################################################################################################################################################################################################
img1 = visual.ImageStim(win=win, image=img1_path, size=2)
img1.draw()
win.flip()
event.waitKeys()
img2 = visual.ImageStim(win=win, image=img2_path, size=2)
img2.draw()
win.flip()
event.waitKeys()
img3 = visual.ImageStim(win=win, image=img3_path, size=2)
img3.draw()
win.flip()
event.waitKeys()
img4 = visual.ImageStim(win=win, image=img4_path, size=2)
img4.draw()
win.flip()
event.waitKeys()

probabilities = [0.7, 0.6, 0.5, 0.4]
random.shuffle(probabilities)
second_mx_idx = probabilities.index(0.6)
mx_idx = probabilities.index(0.7)
################################################################################################################################################################################################
#                                                                                       FIRST BLOCK
################################################################################################################################################################################################
for trial in range(b_trial[0]):
    chosen_index, choice_rt, conf, conf_rt = get_participant_choice()
    chosen_card_pos = cards[chosen_index].pos
    if random.random() <= probabilities[chosen_index]:
        cards[chosen_index].setLineColor('BlueViolet')
        coin.pos = (chosen_card_pos[0], chosen_card_pos[1] - 0.55)
        coin.draw()
        outcome = 'win'
    else:
        cards[chosen_index].setLineColor('BlueViolet')
        red_cross.pos = (chosen_card_pos[0], chosen_card_pos[1] - 0.55)
        red_cross.draw()
        outcome = 'lose'
    for card in cards:
        card.draw()
    # cards[chosen_index].draw()
    win.flip()
    core.wait(2.0) 
    for card in cards:
        card.setFillColor('grey')
        card.setLineColor('grey')
    message = visual.TextStim(win, text='Press SPACE to continue ', pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    results.append({'trial': trial, 'choice': chosen_index, 'outcome': outcome, 'choice_rt': choice_rt, 'confidence_level': conf, 'confidence_rt': conf_rt, 'chosen_agent': '-', 'agent_choices': '-', 'ag_choice_rt': '-', 'trial_type': '1', 'next_trial_rt': sp_rt, 'watch_agent_rt': '-', 'card probs': probabilities, 'agent types': '-'})
################################################################################################################################################################################################
#                                                                                      SECOND BLOCK
################################################################################################################################################################################################
img5 = visual.ImageStim(win=win, image=img5_path, size=2)
img5.draw()
win.flip()
event.waitKeys()
img6 = visual.ImageStim(win=win, image=img6_path, size=2)
img6.draw()
win.flip()
event.waitKeys()
img7 = visual.ImageStim(win=win, image=img7_path, size=2)
img7.draw()
win.flip()

probabilities = [0.7, 0.6, 0.5, 0.4]
random.shuffle(probabilities)
second_mx_idx = probabilities.index(0.6)
mx_idx = probabilities.index(0.7)

event.waitKeys()
for card in cards:
    card.setFillColor('Azure')
    card.setLineColor('Azure')
    
decision_style = [0, 1, 2]
random.shuffle(decision_style)
for trial in range(b_trial[0], b_trial[1]):
    A_choice = e_greedy(0.8, mx_idx)
    B_choice = e_second_greedy(0.6, second_mx_idx)
    C_choice = random.choice([0, 1, 2, 3])
    ch = [A_choice, B_choice, C_choice]
    choices = '-'
    wait_rt = '-'
    if trial % 3 == 0:
        choices = [ch[decision_style[0]], ch[decision_style[1]], ch[decision_style[2]]]
        wait_rt = show_agents_choices(ch[decision_style[0]], ch[decision_style[1]], ch[decision_style[2]], color='Azure')
    chosen_index, choice_rt, conf, conf_rt = get_participant_choice()
    chosen_card_pos = cards[chosen_index].pos
    
    if random.random() < probabilities[chosen_index]:
        cards[chosen_index].setLineColor('BlueViolet')
        coin.pos = (chosen_card_pos[0], chosen_card_pos[1] - 0.55)
        coin.draw()
        outcome = 'win'
    else:
        red_cross.pos = (chosen_card_pos[0], chosen_card_pos[1] - 0.55)
        red_cross.draw()
        cards[chosen_index].setLineColor('BlueViolet')
        outcome = 'lose'
    for card in cards:
        card.draw()
    # cards[chosen_index].draw()
    win.flip()
    core.wait(1.0)
    for card in cards:
        card.setFillColor('Azure')   
        card.setLineColor('Azure')
    message = visual.TextStim(win, text='Press SPACE to continue ', pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    results.append({'trial': trial, 'choice': chosen_index, 'outcome': outcome, 'choice_rt': choice_rt, 'confidence_level': conf, 'confidence_rt': conf_rt, 'chosen_agent': '-', 'agent_choices': choices,  'ag_choice_rt': '-', 'trial_type': '2', 'next_trial_rt': sp_rt, 'watch_agent_rt': wait_rt, 'card probs': probabilities, 'agent types': decision_style})
################################################################################################################################################################################################
#                                                                                      THIRD BLOCK
################################################################################################################################################################################################
img8 = visual.ImageStim(win=win, image=img8_path, size=2)
img8.draw()
win.flip()
event.waitKeys()
img9 = visual.ImageStim(win=win, image=img9_path, size=2)
img9.draw()
win.flip()

probabilities = [0.7, 0.6, 0.5, 0.4]
random.shuffle(probabilities)
second_mx_idx = probabilities.index(0.6)
mx_idx = probabilities.index(0.7)

for card in cards:
    card.setFillColor('BlanchedAlmond')   
    card.setLineColor('BlanchedAlmond')

event.waitKeys()

for trial in range(b_trial[1], b_trial[2]):
    A_choice = e_greedy(0.8, mx_idx)
    B_choice = e_second_greedy(0.6, second_mx_idx)
    C_choice = random.choice([0, 1, 2, 3])
    ch = [A_choice, B_choice, C_choice]
    chosen_agent = '-'
    rt = '-'
    choice = '-'
    wait_rt = '-'
    if trial % 3 == 0:
        chosen_agent, chosen_agent_idx, rt = which_agent()
        if chosen_agent_idx != 3:
            choice = ch[decision_style[chosen_agent_idx]]
            agent_choice = ch[decision_style[chosen_agent_idx]]
            wait_rt = show_chosen_agent(chosen_agent, agent_choice, 'BlanchedAlmond')
    chosen_index, choice_rt, conf, conf_rt = get_participant_choice() 
    chosen_card_pos = cards[chosen_index].pos
      
    if random.random() < probabilities[chosen_index]:
        cards[chosen_index].setLineColor('BlueViolet')
        coin.pos = (chosen_card_pos[0], chosen_card_pos[1] - 0.55)
        coin.draw()
        outcome = 'win'
    else:
        cards[chosen_index].setLineColor('BlueViolet')
        red_cross.pos = (chosen_card_pos[0], chosen_card_pos[1] - 0.55)
        red_cross.draw()
        outcome = 'lose'
    for card in cards:
        card.draw()   
    # cards[chosen_index].draw()
    win.flip()
    core.wait(1.0)
    
    for card in cards:
        card.setFillColor('BlanchedAlmond')
        card.setLineColor('BlanchedAlmond')
    message = visual.TextStim(win, text='Press SPACE to continue ', pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    results.append({'trial': trial, 'choice': chosen_index, 'outcome': outcome, 'choice_rt': choice_rt, 'confidence_level': conf, 'confidence_rt': conf_rt, 'chosen_agent': chosen_agent, 'agent_choices': choice, 'ag_choice_rt': rt, 'trial_type': '3', 'next_trial_rt': sp_rt, 'watch_agent_rt': wait_rt, 'card probs': probabilities, 'agent types': decision_style})
win.close()
################################################################################################################################################################################################
#                                                                                         RESULTS
################################################################################################################################################################################################
# task_info = [
#     ['card_prob', 'agent_type'],
#     [probabilities[0], decision_style[0]],
#     [probabilities[1], decision_style[1]],
#     [probabilities[2], decision_style[2]],
#     [probabilities[3], '-']
# ]
result_dataframe = pd.DataFrame(results)
file_name = path+'subject' + subject_id +'.csv'
result_dataframe.to_csv(file_name, index=False)
# info_file = path+'subject' + subject_id +'info.csv'
# with open(info_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(task_info)