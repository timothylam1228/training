#display image and text in a window
from email.policy import default
import cv2
import os
import PySimpleGUI as sg
from os import path


  
def display(image, text):
    # print(image)
    layout = [[sg.Image(image)],
            [sg.Text('Enter Text'), sg.InputText(text, key='text')],
            [sg.Button('Ok')] ]
    image = cv2.imread('origin_data/'+image)
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        print(event, values)
        if(event == 'Ok'):
            print(values['text'])
            break
        # print('You entered ', values[0])
    window.close()
    return values['text']

#
#for loop
# #
for images in os.listdir('origin_data'):
    if(images == '.DS_Store'):
        continue
    print(images)
    #get filename without extension
    filename = os.path.splitext(images)[0]
    image = path.join('origin_data', images)
    text = open('images_text/'+filename+'.png.gt.txt','r').read()
    # print(text.read())
    firm_text = display(image, text)
    with open('firmed_data/'+filename+'.png.gt.txt', 'w') as file:
        file.write(firm_text)
    # os.remove('images_text/'+filename+'.png.gt.txt')
    os.rename("origin_data/"+filename+'.png', "firmed_image/"+filename+'.png')

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.


# Create the Window

# Event Loop to process "events" and get the "values" of the inputs

