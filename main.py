import os
import pygame
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = '/Generated'
PASSED = '/Passed'
BURNT = '/Burnt'

def get_image_paths():
  images = []
  for subdir, dirs, files in os.walk(ROOT + TARGET):
    for file in files:
      path = os.path.join(subdir, file)
      if path.endswith('.png'):
        images.append({'dir': subdir, 'img_path': path})
  images = sorted(images, key=lambda d: d['dir'])
  return images

def main():
  image_paths = get_image_paths()

  pygame.init()
  white = (255, 255, 255)

  X = 800
  Y = 800

  display_surface = pygame.display.set_mode((X, Y))

  pygame.display.set_caption('Image')

  counter = 0
  image = pygame.image.load(image_paths[counter]['img_path'])
  while True:
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
      print(image_paths[counter])
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == 121 or event.key == 1073741904:
          shutil.move(image_paths[counter]['img_path'], ROOT + PASSED)
          print('Y')
          counter += 1
        elif event.key == 110 or event.key == 1073741903:
          shutil.move(image_paths[counter]['img_path'], ROOT + BURNT)
          print('N')
          counter += 1
        else:
          print('Only Y/N and left/right arrow keys are accepted')


      if counter >= len(image_paths):
        print('Done!')
        pygame.quit()
        quit()

      image = pygame.image.load(image_paths[counter]['img_path'])
      pygame.display.update()

if __name__ == "__main__":
  main()