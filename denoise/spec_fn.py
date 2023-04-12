import os
from scipy.io import wavfile
import noisereduce as nr

def reduce_noise_in_folder(input_folder, output_folder):
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a WAV file
        if filename.endswith(".wav"):
            # Load the WAV file
            input_file = os.path.join(input_folder, filename)
            rate, data = wavfile.read(input_file)

            # Perform noise reduction
            reduced_noise = nr.reduce_noise(y=data, sr=rate)

            # Write the reduced noise data to a new WAV file in the output folder
            output_file = os.path.join(output_folder, filename)
            wavfile.write(output_file, rate, reduced_noise)
