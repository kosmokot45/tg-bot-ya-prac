import ffmpeg
import speech_recognition as sr
import subprocess

# with open('audio/489.ogg') as file_i:
path_to_file = 'audio/489.ogg'

stream = ffmpeg.input(path_to_file)
stream = ffmpeg.output(stream, path_to_file.replace(".ogg", ".wav"), format='wav')
ffmpeg.run(stream)