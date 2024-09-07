from moviepy.editor import *

# Audio
clip1=VideoFileClip("video.mp4").subclip(0,20)
clip1.audio.write_audiofile("test1.mp3")

clip2=VideoFileClip("video2.mp4").subclip(0,20)
clip2.audio.write_audiofile("test2.mp3")

# Video
clip3=VideoFileClip("video.mp4").subclip(0,20)
clip3=clip3.without_audio()
clip3.write_videofile("generated.mp4")

video_file=VideoFileClip("generated.mp4")
audio_file=AudioFileClip("test2.mp3")

# Putting the extracted audio into generated video
final_video=video_file.set_audio(audio_file)
final_video.write_videofile("swapped.mp4")