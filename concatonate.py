# Micah Scott - 1-16-19
# this program concatonates video clips as designated by the user and saves
# them into a 'final_folder' directory where this .py is located

#from moviepy.editor import VideoFileClip, concatonate_videoclips
from moviepy.editor import *
from os import *
from sys import *

#this will list the availbale mp4s from the dir specified below
print('\n\nAvailable mp4s:\n')
for x in os.listdir('./sample_mp4s'):
    print(x)

#promt user
user_choice1 = input('select a video for clip1 >\n')
user_choice2 = input('select a video for clip2 >\n')
user_choice3 = input('select a video for clip3 >\n')

#"parse" the user input into the proper format 
user_choice10 = str('sample_mp4s/' + user_choice1)
user_choice20 = str('sample_mp4s/' + user_choice2)
user_choice30 = str('sample_mp4s/' + user_choice3)

#redefine the new file name and location
clip1 = VideoFileClip(user_choice10)
clip2 = VideoFileClip(user_choice20)
clip3 = VideoFileClip(user_choice30)

#allow the user to name the file so they can find it easier later
new_file_name = input('What do you want to name your new creation? >\n (don''t forget to make it a .mp4!!!)\n')
new_file_location = str('final_folder/' + new_file_name)

#concatenate the selected mp4s and save the new file to the 'final_folder' directory
final_clip = concatenate_videoclips([clip1, clip2, clip3], method='compose')
final_clip.write_videofile(new_file_location)



#clip = VideoFileClip('sample_mp4s/Raptor.mp4')
#clip.preview()    this is an example of how to use the preview module