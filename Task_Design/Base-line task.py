from psychopy import visual, event, data, core
import random
import pandas as pd


img1_path = 'D:/University/MSc/Thesis/task/Images/bl1.png'
img2_path = 'D:/University/MSc/Thesis/task/Images/bl2.png'
img3_path = 'D:/University/MSc/Thesis/task/Images/bl3.png'
img4_path = 'D:/University/MSc/Thesis/task/Images/bl4.png'
img5_path = 'D:/University/MSc/Thesis/task/Images/bl5.png'
img6_path = 'D:/University/MSc/Thesis/task/Images/bl6.png'
bl_path = 'D:/University/MSc/Thesis/task/Images/bl.png'

b_trial = [15, 45, 105]

subject_id = '41'

path = 'D:/University/MSc/Thesis/task/data/base-line/4 arm/'

win = visual.Window([1707, 1067], color="Black", fullscr=True)
reaction_clock = core.Clock()


cards = [visual.Rect(win, width=0.3, height=0.8, pos=[-0.75, 0], lineWidth=5, fillColor='grey'),
         visual.Rect(win, width=0.3, height=0.8, pos=[-0.25, 0], lineWidth=5, fillColor='grey'),
         visual.Rect(win, width=0.3, height=0.8, pos=[0.25, 0], lineWidth=5, fillColor='grey'),
         visual.Rect(win, width=0.3, height=0.8, pos=[0.75, 0], lineWidth=5, fillColor='grey')]

social_cards = [visual.Rect(win, width=0.3, height=0.8, pos=[-0.75, 0], lineColor='BlueViolet'),
                visual.Rect(win, width=0.3, height=0.8, pos=[-0.25, 0], lineColor='BlueViolet'),
                visual.Rect(win, width=0.3, height=0.8, pos=[0.25, 0], lineColor='BlueViolet'),
                visual.Rect(win, width=0.3, height=0.8, pos=[0.75, 0], lineColor='BlueViolet')]

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
imgbl = visual.ImageStim(win=win, image=bl_path, size=2)
imgbl.draw()
win.flip()
event.waitKeys()
win.flip()

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
    results.append({'trial': trial, 'choice': chosen_index, 'outcome': outcome, 'choice_rt': choice_rt, 'confidence_level': conf, 'confidence_rt': conf_rt, 'next_trial_rt': sp_rt, 'card probs': probabilities})
    
################################################################################################################################################################################################
#                                                                                       SECOND BLOCK
################################################################################################################################################################################################

img3 = visual.ImageStim(win=win, image=img3_path, size=2)
img3.draw()
win.flip()
event.waitKeys()
img4 = visual.ImageStim(win=win, image=img4_path, size=2)
img4.draw()
win.flip()


probabilities = [0.7, 0.6, 0.5, 0.4]
random.shuffle(probabilities)
second_mx_idx = probabilities.index(0.6)
mx_idx = probabilities.index(0.7)

event.waitKeys()
for card in cards:
    card.setFillColor('Azure')
    card.setLineColor('Azure')
    
for trial in range(b_trial[0], b_trial[1]):
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
        card.setFillColor('Azure')
        card.setLineColor('Azure')
    message = visual.TextStim(win, text='Press SPACE to continue ', pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    results.append({'trial': trial, 'choice': chosen_index, 'outcome': outcome, 'choice_rt': choice_rt, 'confidence_level': conf, 'confidence_rt': conf_rt, 'next_trial_rt': sp_rt, 'card probs': probabilities})
    
################################################################################################################################################################################################
#                                                                                      THIRD BLOCK
################################################################################################################################################################################################

img5 = visual.ImageStim(win=win, image=img5_path, size=2)
img5.draw()
win.flip()
event.waitKeys()
img6 = visual.ImageStim(win=win, image=img6_path, size=2)
img6.draw()
win.flip()


probabilities = [0.7, 0.6, 0.5, 0.4]
random.shuffle(probabilities)
second_mx_idx = probabilities.index(0.6)
mx_idx = probabilities.index(0.7)

event.waitKeys()
for card in cards:
    card.setFillColor('BlanchedAlmond')
    card.setLineColor('BlanchedAlmond')


for trial in range(b_trial[1], b_trial[2]):
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
        card.setFillColor('BlanchedAlmond')
        card.setLineColor('BlanchedAlmond')
    message = visual.TextStim(win, text='Press SPACE to continue ', pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    space_key = event.waitKeys(keyList=['space'], timeStamped=reaction_clock)
    _, sp_rt = space_key[-1]
    results.append({'trial': trial, 'choice': chosen_index, 'outcome': outcome, 'choice_rt': choice_rt, 'confidence_level': conf, 'confidence_rt': conf_rt, 'next_trial_rt': sp_rt, 'card probs': probabilities})
    
    
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