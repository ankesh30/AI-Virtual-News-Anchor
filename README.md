**AI Virtual News Anchor:**

An AI-powered virtual news anchor system that automatically fetches news articles based on topic and count, 
converts them to speech using Text-to-Speech, and generates a fully lip-synced video using an AI avatar. 
This system is designed to simulate a realistic news presentation experience and includes a user-friendly GUI for input control.

Features
GUI-based interface for manual or automated news input
Automatic news fetching from Google News based on topic and count
Text-to-speech synthesis using gTTS (Google Text-to-Speech)
Lip-synced avatar video generation using Wav2Lip
Background audio-video merging
Final AI-anchored news video output

**Project Structure**

AI-Virtual-News-Anchor/
<br>
│
<br>
├── gui.py  --------->                         # GUI interface built with Tkinter for user interaction and news input
<br>
├── main.py   ------->                       # Main controller script that integrates all modules and triggers the complete pipeline
<br>
├── boundary_box_detection.py  ------->      # Script to detect bounding box coordinates for lips, chin, and cheeks of the avatar image
<br>
├── avatar.jpg  ------->                     # Static avatar image used to generate the lip-synced talking head
<br>
├── project GUI screenshot.png ------>      # Screenshot of the GUI to provide a visual preview of the interface
<br>
│
<br>
├── Wav2Lip/ -------> Deep Learning model, that generate the lip-sync video from the image given by the user.
<br>
│   └── inference.py     ------>            # Lip-sync video generation module using Wav2Lip model
<br>
│
<br>
├── modules/
<br>
│   ├── text_generation.py  ------->        # Automatically fetches and generates news content using web scraping and APIs
<br>
│   ├── text_to_speech.py ------->          # Converts generated or manually input news text into speech using gTTS
<br>
│   └── avatar_generation.py ------->       # Coordinates the avatar image and speech audio to generate the final video
<br>
│
<br>
├── output/
<br>
│   └── result_voice.mp4  -------->          # Final output video of the AI avatar reading the news with lip-sync
<br>
│
<br>
├── requirements.txt     ------->           # List of required Python libraries and packages to run the project
<br>
└── README.md        --------->               # Project documentation file with setup instructions and project details


**How to Setup and Run the Project**

1. Clone the Repository:
   <br>
"git clone https://github.com/ankesh30/AI-Virtual-News-Anchor.git
<br>
cd AI-Virtual-News-Anchor"
<br>
<br>
3. Create a Virtual Environment (Optional but recommended):

"python -m venv venv
<br>
venv\Scripts\activate    # On Windows
<br>
or
<br>
source venv/bin/activate  # On Linux/Mac"
<br>
<br>
3. Install Dependencies:
<br>
"pip install -r requirements.txt"
<br>
<br>
4. Download Pretrained Wav2Lip Model:
<br>
"Download from: https://github.com/Rudrabha/Wav2Lip"
<br>
Place the Wav2Lip.pth file in the project directory or models folder.
<br>
<br>
5. Run the Project:
<br>
"python gui.py"
<br>
Use the GUI to enter a topic (e.g., Technology), specify the number of news items, and click "Generate News Video".
<br>
<br>
**Output**
<br>
Final output video: output/result_voice.mp4
<br>
Description: This file is the final result of the AI Virtual News Anchor project. It contains the AI avatar speaking the selected or auto-fetched news in a realistic lip-synced video format.
<br>
<br>
**Dependencies**
<br>
Python 3.7+
<br>
gTTS
<br>
moviepy
<br>
OpenCV
<br>
numpy
<br>
requests
<br>
newspaper3k
<br>
GoogleNews
<br>
tqdm
<br>
torch, torchvision
<br>
ffmpeg (installed and added to system path)
<br>

**Install all via:**
<br>
"pip install -r requirements.txt"
<br>
<br>
**External Libraries / APIs Used**
<br>
gTTS (Google Text-to-Speech) - For speech generation
<br>
Wav2Lip - For generating lip-synced videos
<br>
GoogleNews API - For fetching latest news headlines
<br>
newspaper3k - For extracting full news articles
<br>
<br>

**Screenshots / Demo**
<br>
Figure: Project GUI with topic input and generation buttons
<br>
GUI Preview:
<br>
GUI Screenshot-->(AI-Virtual-News-Anchor/Project GUI ScreenSort.png)
<br>
<br>

Figure: Frame from final result_voice.mp4 video
<br>
see the final result video -- AI-Virtual-News-Anchor/output/result_voice.mp4
<br>
<br>

**Author**
<br>
Ankesh Agrawal
<br>
B.Tech in Artificial Intelligence and Machine Learning.
<br>
<br>
**Submission Note**
<br>
This repository is publicly accessible for evaluation.
<br>
All required libraries and APIs are included or referenced.
<br>
GUI of the project is located at project GUI screenshot.png for easy validation.
<br>
Final video output is located at output/result_voice.mp4 for easy validation.
<br>
<br>
For any queries or issues, please contact via GitHub issues or pull request.
