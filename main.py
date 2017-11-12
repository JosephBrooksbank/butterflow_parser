from moviepy.editor import VideoFileClip
import subprocess
import os
videoName = "test.mp4"

clip = VideoFileClip(videoName)
videoDuration = clip.duration

numberOfClips = videoDuration / 5
cwd = os.getcwd()
butterflowDir = cwd + "\\butterflow-0.2.3"

subprocess.call(butterflowDir + "\\butterflow -v -r 60 " + videoName + " -o output.mp4", shell=True)



