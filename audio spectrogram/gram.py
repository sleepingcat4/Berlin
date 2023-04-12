import os
import matplotlib.pyplot as plt

import librosa
from librosa.display import waveplot

def create_log_spectrograms(input_folder, output_folder):
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a WAV file
        if filename.endswith(".wav"):
            # Load the audio file
            audio_path = os.path.join(input_folder, filename)
            x, sr = librosa.load(audio_path, sr=44100)

            # Create the logarithmic spectrogram
            X = librosa.stft(x)
            Xdb = librosa.amplitude_to_db(abs(X))

            # Plot the spectrogram
            plt.figure(figsize=(14, 5))
            librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
            plt.colorbar()

            # Save the plot to an image file in the output folder
            output_path = os.path.join(output_folder, filename[:-4] + ".png")
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
