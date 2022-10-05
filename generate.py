import os
#read firmed_image and firmed_data and change them into one txt file

#open firmed_image folder
for images in os.listdir('firmed_image'):
    #get filename without extension
    filename = os.path.splitext(images)[0]
    #get file path
    image = os.path.join('firmed_image', images)
    #read firmed_data file
    text = open('firmed_data/'+filename+'.png.gt.txt','r').read()
    #write into one txt file
    with open('firmed_data.txt', 'a') as file:
        file.write(image+' '+text+'\n')
