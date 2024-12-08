from pathlib import Path
from openai import OpenAI

client = OpenAI()

# Define the path to the input text file and the output audio file
text_file_path = Path(__file__).parent / "input_text.txt"
speech_file_path = Path(__file__).parent / "audio.mp3"

# Read the text content from the file
with open(text_file_path, "r") as file:
    text_content = file.read()

# Generate the speech
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text_content
)

# Save the audio to a file
response.stream_to_file(speech_file_path)
