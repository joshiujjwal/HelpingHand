import speech_recognition as sr

import os

from pydub import AudioSegment
from pydub.silence import split_on_silence

from youtube_transcript_api import YouTubeTranscriptApi
import dequeue



video_id_list ={"knitting":'PLYfCBK8IplO6v0QjCj-TSrFUXnRV0WxfE'}
for id,value in video_id_list.items():
    dict =YouTubeTranscriptApi.get_transcript("sF_jSrBhdlg&list="+value)
    file = open(r"transcript"+id+".txt", "a+")

for i in dict:
    file.write(i["text"]+"\n")
file.close()

video_id_list = {}


