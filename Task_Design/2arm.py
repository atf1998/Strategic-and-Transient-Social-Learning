from psychopy import visual, event, data, core
import random
import pandas as pd 

path = 'D:/University/MSc/Thesis/task/Final version/data/'
img1_path = 'D:/University/MSc/Thesis/task/Images/2arm1.png'
subject_id = '41'
num_trials = 30
group = 3

if group == 1:
    path = 'D:/University/MSc/Thesis/task/data/trained/2 arm/'
elif group == 2:
    path = 'D:/University/MSc/Thesis/task/data/not trained/2 arm/'
else:
    path = 'D:/University/MSc/Thesis/task/data/base-line/2 arm/'

win = visual.Window([1707, 1067], color="Black", fullscr=True)
reaction_clock = core.Clock()
options = [visual.Circle(win, radius=0.3, pos=[-0.45, 0], fillColor='grey'),
           visual.Circle(win, radius=0.3, pos=[0.45, 0], fillColor='grey')]

probs = [0.6, 0.8]
random.shuffle(probs)
best_idx = probs.index(max(probs))
result = []

#######################################################################################
#                                     FUNCTIONS
#######################################################################################
def get_participant_choice():
    txt = 'Press f for the left card and j for the right card'
    message = visual.TextStim(win, text=txt, pos=(0, 0.6))
    message.draw()
    for option in options:
        option.draw()
    win.flip()
    reaction_clock.reset()
    choice = None
    conf = None
    while choice not in ['f', 'j']:
        keys = event.waitKeys(timeStamped=reaction_clock)
        if keys:
            choice, choice_rt = keys[0]
    txt = 'Press 1, 2, 3, 4 or 5 as your confidence'
    message = visual.TextStim(win, text=txt, pos=(0, 0))
    message.draw()
    win.flip()
    reaction_clock.reset()
    while conf not in ['1', '2', '3', '4', '5']:
        conf_keys = event.waitKeys(timeStamped=reaction_clock)
        if conf_keys:
            conf, conf_rt = conf_keys[0]
    if choice == 'f':
        choice_idx = 0
    else:
        choice_idx = 1
    return choice_idx, choice_rt, conf, conf_rt
    
#######################################################################################
#                                     MAIN
#######################################################################################
img1 = visual.ImageStim(win=win, image=img1_path, size=2)
img1.draw()
win.flip()
event.waitKeys()
for trial in range(num_trials):
    sub_choice, sub_choice_rt, sub_conf, sub_conf_rt = get_participant_choice()
    if random.random() <= probs[sub_choice]:
        options[sub_choice].setFillColor('green')
        outcome = 'win'
    else:
        options[sub_choice].setFillColor('red')
        outcome = 'lose'
    options[sub_choice].draw()
    win.flip()
    core.wait(2.0)
    
    result.append({'trial': trial, 'choice': sub_choice, 'outcome': outcome, 'choice_rt': sub_choice_rt, 'confidence_level': sub_conf, 'confidence_rt': sub_conf_rt, 'probs': probs})
    for option in options:
        option.setFillColor('grey')
        
        
        
result_dataframe = pd.DataFrame(result)
file_name = path+'subject' + subject_id +'_2arm.csv'
result_dataframe.to_csv(file_name, index=False)
