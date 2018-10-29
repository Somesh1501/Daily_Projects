import os

file_path = '/home/ironman/Pictures/wallpapers'
count = 0

for folder, subfolder, files in os.walk(file_path):
    for file in files:
        name = 'Wallpaper_{}'.format(count)
        os.rename(file, name)
        print('Renaming {} with {}'.format(file, name))
        count += 1
