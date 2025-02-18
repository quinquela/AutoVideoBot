Video Meme Generator
This project automates the process of creating videos with memes by selecting a video, adding a caption (meme text) to it, and combining it with an audio file. It interacts with a JSON file to retrieve video paths, descriptions, and recommendations, and then uses the Gemini AI model to generate meme captions. The video is then edited using FFmpeg to add the meme text and a random audio track.

Features
Selects videos from a JSON file based on user input.
Uses the Gemini AI model to generate meme text based on video descriptions, recommendations, and examples.
Edits videos by adding meme text and synchronizing with audio.
Supports automatic video scaling and padding to ensure proper aspect ratio.
Randomly selects background music for each video.
Outputs edited videos in MP4 format.
Requirements
Python 3.x
FFmpeg (ensure it's installed and accessible in your system)
Google Gemini API Key (stored in .env file)
Python libraries:
google
ffmpeg-python
dotenv
json
os
random
You can install the necessary libraries using:

bash
Copiar
Editar
pip install google ffmpeg-python python-dotenv
Setup
Clone this repository or download the files.

Install the required Python libraries.

Place your API key for Gemini in a .env file:

ini
Copiar
Editar
API_KEY=your_gemini_api_key
Add your video files and audio clips to the appropriate directories.

Ensure that the JSON file (ejemplosVideos.json) is formatted correctly with video paths, descriptions, recommendations, and examples.

How to Use
Run the main.py script:

bash
Copiar
Editar
python main.py
The script will ask for the number of videos to process and the language in which to generate the meme text.

Based on your input, the script will:

Select videos from the JSON file.
Use Gemini AI to generate meme text.
Add the meme text to the video, scale it to 1080x1920 resolution (portrait mode), and add random background music.
Save the edited video in the outputVideos folder.
File Structure
css
Copiar
Editar
.
├── audios/
│   ├── disturbing_the_peaceeeee (mp3cut.net).mp3
│   ├── a.mp3
│   ├── b.mp3
│   ├── c.mp3
│   ├── d.mp3
├── ejemplosVideos.json
├── outputVideos/
├── fuente/
│   ├── Open_Sans/
│   ├── OpenSans-Italic-VariableFont_wdth,wght.ttf
├── main.py
├── .env
JSON Format
The JSON file (ejemplosVideos.json) should have the following structure:

json
Copiar
Editar
{
    "video1": {
        "file_path": "videos/video1.mp4",
        "description": "A funny video about coding.",
        "recommendation": "Watch this video if you like programming.",
        "example": "A programmer's life."
    },
    "video2": {
        "file_path": "videos/video2.mp4",
        "description": "A funny video about debugging.",
        "recommendation": "Watch this video if you like solving problems.",
        "example": "Every bug has a solution."
    }
}
Contributing
Feel free to contribute to this project by submitting issues or pull requests. Please make sure your contributions align with the overall functionality of the project.

License
This project is licensed under the MIT License - see the LICENSE file for details.

