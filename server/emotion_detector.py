#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import load_model


# In[2]:


emotion_classifier = load_model("Emotion_Audio.h5", compile=False)


# In[4]:


#pip install librosa


# In[5]:


import numpy as np
import pandas as pd
import librosa


# In[6]:


def extract_features(data,sample_rate):
    # ZCR
    result = np.array([])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result=np.hstack((result, zcr)) # stacking horizontally

    # Chroma_stft
    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally

    # Root Mean Square Value
    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    
    return result


# In[12]:


import pyaudio
import tensorflow
import wave
from tensorflow.image import resize
from scipy.ndimage import zoom
def get_audio():
    Chunk = 1024
    Format = pyaudio.paInt16
    Channels = 1
    Rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=Format, channels=Channels, rate=Rate, input=True, frames_per_buffer=Chunk)
    frames = []
    seconds = 3

    print("Recording started")
    for i in range(0, int(Rate / Chunk * seconds)):
        data = stream.read(Chunk)
        frames.append(data)

    print("Recording stopped")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open("o.wav",'wb')
    wf.setnchannels(Channels)
    wf.setsampwidth(p.get_sample_size(Format))
    wf.setframerate(Rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    audio_data = b"".join(frames)  # Combine the recorded frames into a single byte string

    # Convert the byte string to a NumPy array of int16
    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # Convert the int16 array to floating-point values between -1 and 1
    audio_array = audio_array.astype(np.float32) / 32768.0
    # Compute MFCC
    mfcc = extract_features(audio_array,Rate)

    # Add an extra dimension to match the expected input shape of the "DCNN" layer
    mfcc0 = np.resize(mfcc,(162,1))
    mfcc_reshaped = np.reshape(mfcc0, (1, 162, 1))
    x=emotion_classifier(mfcc_reshaped)
    emotion_code=np.argmax(x,axis=1)
    return emotion_code


# In[15]:





# In[ ]:




