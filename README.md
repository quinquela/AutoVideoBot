## Auto vid

Autovid is a program that automates the creation of shorts/reels/TikToks or videos for any type of social media with vertical format videos. The program selects the video and music, then generates a joke, and finally edits the video automatically.

### Requirements
- Python 3.x
- Google Gemini API key (you must place it in the .env)
- Python libraries
  - google
  - ffmpeg-python
  - python_dotenv
  - json
  - os
  - random

### JSON Format:
```json
{
    "video1": {
        "file_path": "videos/video1.mp4",
        "description": "A funny video about coding.",
        "recommendation": "make a joke about coding.",
        "example": "A programmer's life."
    },
    "video2": {
        "file_path": "videos/video2.mp4",
        "description": "A funny video about debugging.",
        "recommendation": "make a joke about  how difficult is debugging.",
        "example": "Every bug has a solution."
    }
}
```

### Contributions
Feel free to contribute and make a pull request to the project. Please ensure that your contribution aligns with the project's purpose.

## Instalation and configuration
1. Clone the repository
   ```bash git clone https://github.com/tu-usuario/AutoVid.git ```
2. Install the necessary libraries by running the following command: ```bash pip install google ffmpeg-python python-dotenv  ``` 
3. Create a `.env` file and place your Google Gemini API key there. 

   
3. 
### Usage:
1. When you run it, it will ask you how many videos you want to generate.
2. Then, it will ask you to choose the language.
3. Once you fill in this information, the videos will be created in the `outputVideos` folder.
![image](https://github.com/user-attachments/assets/07760818-5d62-456c-9fd9-4b7412a438dc)

### License
The project uses the MIT License.
