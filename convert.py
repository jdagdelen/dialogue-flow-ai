from pydub import AudioSegment
import os

# Set the directory path where the mp3 files are located
mp3_dir = 'tracks_mp3'

# Set the directory path where the wav files will be saved
wav_dir = 'tracks_wav'

# Loop through all the files in the directory
for filename in os.listdir(mp3_dir):
    # Check if the file is an mp3 file
    if filename.endswith('.mp3'):
        # Load the mp3 file
        mp3_path = os.path.join(mp3_dir, filename)
        audio = AudioSegment.from_mp3(mp3_path)
        
        # Create the output filename
        wav_filename = filename[:-4] + '.wav'
        wav_path = os.path.join(wav_dir, wav_filename)
        
        # Export the wav file
        audio.export(wav_path, format='wav')
