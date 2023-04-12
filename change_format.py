from pydub import AudioSegment

# Load AAC file
audio = AudioSegment.from_file('audio_noise.aac', format='aac')

# Export as WAV file
audio.export('audio_file.wav', format='wav')
