# subtitle-Generator-using-DeepSpeech

This project provides a simple Python tool to transcribe audio from audio or video files and generate subtitle files in `.srt` format. It uses the [DeepSpeech](https://github.com/mozilla/DeepSpeech) model for transcription and `ffmpeg` for extracting audio from video files.

## Features:
- **Audio Transcription:** Converts speech from audio files into text using the DeepSpeech model.
- **Video to Audio Conversion:** Extracts audio from video files before transcription.
- **Subtitle Generation:** Creates `.srt` subtitle files from transcription JSON output.

## Requirements:

### Dependencies:
- Python 3.10 (or compatible versions)
- `ffmpeg` for audio extraction from video files
- DeepSpeech pre-trained model and scorer for transcription

### Installation:
1. **Clone the repository:**
   ```bash
  git clone https://github.com/rdss1027/subtitle-Generator-using-DeepSpeech.git
   cd audio-video-transcription

### Set up a Python virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # For Windows, use: venv\Scripts\activate

Install the required Python dependencies: Ensure requirements.txt is in the project directory and install the dependencies:

pip install -r requirements.txt

### Download DeepSpeech model and scorer:

  Go to the DeepSpeech releases page.
    Download the latest pre-trained model (e.g., deepspeech-0.9.3-models.pbmm) and scorer (e.g., deepspeech-0.9.3-models.scorer).
        You can download the .pbmm and .scorer files from this link: DeepSpeech Model & Scorer.
    After downloading, place the deepspeech-0.9.3-models.pbmm and deepspeech-0.9.3-models.scorer files in the models directory within your project folder.

# Your project folder structure should look like this:

   /audio-video-transcription
    ├── input_files/            # Place your input audio or video files here
    ├── models/                 # Place DeepSpeech model files here
    │   ├── deepspeech-0.9.3-models.pbmm
    │   └── deepspeech-0.9.3-models.scorer
    ├── output_files/           # Output JSON, audio, and subtitle files
    ├── main.py                 # Python script to run the transcription and subtitle generation
    ├── requirements.txt        # List of Python dependencies
    ├── README.md               # Project description and setup instructions
    └── LICENSE                 # MIT License (or other license you choose)

# Install ffmpeg:
  Follow the instructions on the official website to install ffmpeg.
   Ensure that ffmpeg is accessible from your system’s command line (you can check by running ffmpeg -version).

Usage:

  Prepare your files:
        Place your audio files (e.g., .mp3, .wav, .flac) in the input_files directory.
        If you have video files (e.g., .mp4, .avi, .mov), place them in the same directory.

# Run the script: Execute the main.py script to process your audio or video files and generate subtitles:

  python main.py

  Enter the filename: The script will prompt you to enter the filename (with extension) of your audio or video file. It will process the file and generate the corresponding output JSON and subtitle files.

  Output: The output files will be saved in the output_files directory:
        Transcription output in .json
        Extracted audio from video (if applicable)
        Subtitles in .srt format

Example:

For a video file sample_video.mp4:

  The script will:
        Extract the audio as sample_video_extracted_audio.wav
        Transcribe it into sample_video_output.json
        Generate subtitles in sample_video_subtitles.srt
