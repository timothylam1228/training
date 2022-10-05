import os
import csv

#generate csv according to filename in a folder Passed
ROOT = os.path.dirname(os.path.abspath(__file__))

def get_image_paths():
  images = []
  for subdir, dirs, files in os.walk(ROOT+'/Burnt-1'):
    for file in files:
    
      path = os.path.join(subdir, file)
      if path.endswith('.png'):
        images.append(path.replace(ROOT+'/Burnt-1/',''))
#   images = sorted(images, key=lambda d: d['dir'])
  return images

def generateCSV():
    with open('Passed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        a = get_image_paths()
        for i in range(len(a)):
            print(a[i])
            #save a[i] in a csv file inside a field
            writer.writerow([a[i],1])
            # path = a[i]['img_path'][7:]
            # writer.writerow(a[i])
def generateCSVB():
    with open('Burnt-1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        a = get_image_paths()
        for i in range(len(a)):
            print(a[i])
            #save a[i] in a csv file inside a field
            writer.writerow([a[i],0])
            # path = a[i]['img_path'][7:]
            # writer.writerow(a[i])

        #read all file name in a folder
  
      

# generateCSV()
generateCSVB()