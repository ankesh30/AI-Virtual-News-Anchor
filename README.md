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
│
├── gui.py                           # GUI interface built with Tkinter for user interaction and news input
├── main.py                          # Main controller script that integrates all modules and triggers the complete pipeline
├── boundary_box_detection.py        # Script to detect bounding box coordinates for lips, chin, and cheeks of the avatar image
├── avatar.jpg                       # Static avatar image used to generate the lip-synced talking head
├── project GUI screenshot.png       # Screenshot of the GUI to provide a visual preview of the interface
│
├── Wav2Lip/
│   └── inference.py                 # Lip-sync video generation module using Wav2Lip model
│
├── modules/
│   ├── text_generation.py          # Automatically fetches and generates news content using web scraping and APIs
│   ├── text_to_speech.py           # Converts generated or manually input news text into speech using gTTS
│   └── avatar_generation.py        # Coordinates the avatar image and speech audio to generate the final video
│
├── output/
│   └── result_voice.mp4            # Final output video of the AI avatar reading the news with lip-sync
│
├── requirements.txt                # List of required Python libraries and packages to run the project
└── README.md                       # Project documentation file with setup instructions and project details


**How to Setup and Run the Project**

1. Clone the Repository:

"git clone https://github.com/ankesh30/AI-Virtual-News-Anchor.git
cd AI-Virtual-News-Anchor"

2. Create a Virtual Environment (Optional but recommended):

"python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate  # On Linux/Mac"

3. Install Dependencies:

"pip install -r requirements.txt"

4. Download Pretrained Wav2Lip Model:

"Download from: https://github.com/Rudrabha/Wav2Lip"

Place the Wav2Lip.pth file in the project directory or models folder.

5. Run the Project:

"python gui.py"

Use the GUI to enter a topic (e.g., Technology), specify the number of news items, and click "Generate News Video".

**Output**
Final output video: output/result_voice.mp4
Description: This file is the final result of the AI Virtual News Anchor project. It contains the AI avatar speaking the selected or auto-fetched news in a realistic lip-synced video format.

**Dependencies**
Python 3.7+
gTTS
moviepy
OpenCV
numpy
requests
newspaper3k
GoogleNews
tqdm
torch, torchvision
ffmpeg (installed and added to system path)

**Install all via:**
"pip install -r requirements.txt"

**External Libraries / APIs Used**
gTTS (Google Text-to-Speech) - For speech generation
Wav2Lip - For generating lip-synced videos
GoogleNews API - For fetching latest news headlines
newspaper3k - For extracting full news articles

**Screenshots / Demo**
Figure: Project GUI with topic input and generation buttons
GUI Preview
GUI Screenshot-->(AI-Virtual-News-Anchor/Project GUI ScreenSort.png)

Figure: Frame from final result_voice.mp4 video
see the final result video -- AI-Virtual-News-Anchor/output/result_voice.mp4

**Author**
Ankesh Agrawal
B.Tech in Artificial Intelligence and Machine Learning.

**Submission Note**
This repository is publicly accessible for evaluation.
All required libraries and APIs are included or referenced.
GUI of the project is located at project GUI screenshot.png for easy validation.
Final video output is located at output/result_voice.mp4 for easy validation.

For any queries or issues, please contact via GitHub issues or pull request.
