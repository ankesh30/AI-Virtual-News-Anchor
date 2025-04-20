#import openai
#from config import OPENAI_API_KEY

#openai.api_key = OPENAI_API_KEY


#def text_to_speech(news_text, voice="alloy"):
    #"""Converts given text into speech using OpenAI's text-to-speech API."""
    #response = openai.audio.speech.create(
     #   model="tts-1",
      #  voice=voice,
       # input=news_text
    #)

    # Save the audio file
    #audio_path = "news_audio.mp3"
    #with open(audio_path, "wb") as f:
     #   f.write(response.content)

    #print(f"✅ Speech generated and saved as {audio_path}")
    #return audio_path


# Test the function
#if __name__ == "__main__":
 #   sample_news = "Breaking news! AI-powered virtual anchors are revolutionizing the media industry."
  #  text_to_speech(sample_news)

import os
from gtts import gTTS

def text_to_speech(news_text):
    tts = gTTS(text=news_text, lang="en")
    audio_path = "output.mp3"
    tts.save(audio_path)
    print(f"✅ Audio generated: {audio_path}")

    # Play the generated audio
    os.system(f"start {audio_path}")  # For Windows
    return audio_path



