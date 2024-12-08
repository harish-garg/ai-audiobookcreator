# AI Audiobook Creator

This project transforms text files into high-quality audiobook-style speech using OpenAI's text-to-speech API. Simply provide a text file, and the script generates an `.mp3` file that you can listen to as an audiobook.

## Features
- Converts text files into audiobook-style speech.
- Uses OpenAI's `tts-1` model for natural and clear text-to-speech generation.
- Simple setup and easy to use.

## Requirements
- Python 3.8 or higher.
- An OpenAI API key.

## Installation

1. Clone the repository:
   git clone <repository_url>
   cd <repository_folder>

2. Install dependencies:
    pip install -r requirements.txt

3. Add a text file named input_text.txt in the project directory with the content you want to convert into an audiobook.
4. add your openai api key in your environment variables.

https://zyrae.com
## Usage
1. Write or paste the text of your book or story into input_text.txt.
2. Run the script:
  python main.py

The audiobook will be saved as audio.mp3 in the project directory.
