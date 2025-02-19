import os
import subprocess
import json

def run_deepspeech(audio_filename, output_filename):
    model_path = os.path.join("models", "deepspeech-0.9.3-models.pbmm")
    scorer_path = os.path.join("models", "deepspeech-0.9.3-models.scorer")
    command = f"deepspeech --model {model_path} --scorer {scorer_path} --audio {audio_filename} --json > {output_filename}"
    subprocess.run(command, shell=True)

def extract_audio_from_video(video_filename, extracted_audio_filename):
    command = f"ffmpeg -i {video_filename} -vn -acodec pcm_s16le -ar 16000 -ac 1 {extracted_audio_filename}"
    subprocess.run(command, shell=True)

def json_to_srt(json_file, srt_file):
    with open(json_file) as f:
        data = json.load(f)

    with open(srt_file, "w") as srt:
        for transcript_index, transcript in enumerate(data['transcripts']):
            for i, result in enumerate(transcript['words']):
                start_time = result['start_time']
                end_time = start_time + result['duration']
                word = result['word']

                start_time_srt = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time % 1) * 1000):03}"
                end_time_srt = f"{int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02},{int((end_time % 1) * 1000):03}"

                srt.write(f"{i+1 + transcript_index * 1000}\n")
                srt.write(f"{start_time_srt} --> {end_time_srt}\n")
                srt.write(f"{word}\n\n")

def main():
    input_filename = input("Enter the filename (with extension) of your audio or video file: ")

    if not input_filename:
        print("Error: No filename provided.")
        return

    # Define paths for input and output directories
    input_dir = "input_files"
    output_dir = "output_files"
    models_dir = "models"

    # Ensure the directories exist
    if not os.path.exists(input_dir):
        print(f"Error: The input directory {input_dir} does not exist.")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Form full input file path
    input_filepath = os.path.join(input_dir, input_filename)

    if not os.path.isfile(input_filepath):
        print(f"Error: The file {input_filepath} does not exist.")
        return

    # Base filename without extension
    base_filename = os.path.splitext(input_filename)[0]

    # Check if the input is an audio or video file
    if input_filename.lower().endswith(('.mp3', '.wav', '.flac')):
        output_json = os.path.join(output_dir, base_filename + "_output.json")
        print(f"Processing audio file: {input_filepath}")
        run_deepspeech(input_filepath, output_json)
    elif input_filename.lower().endswith(('.mp4', '.avi', '.mov')):
        extracted_audio = os.path.join(output_dir, base_filename + "_extracted_audio.wav")
        output_json = os.path.join(output_dir, base_filename + "_output.json")
        print(f"Processing video file: {input_filepath}")
        extract_audio_from_video(input_filepath, extracted_audio)
        run_deepspeech(extracted_audio, output_json)
    else:
        print("Error: Unsupported file format. Please provide either an audio or video file.")
        return

    srt_filename = os.path.join(output_dir, base_filename + "_subtitles.srt")
    json_to_srt(output_json, srt_filename)
    print(f"Subtitles have been generated and saved to {srt_filename}.")

if __name__ == "__main__":
    main()
