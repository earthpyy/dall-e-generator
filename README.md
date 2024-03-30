# dall-e-generator

_Note: This repository was developed from [vickypandey14/OpenAI-Dall.E-Image-Generation-in-Python](https://github.com/vickypandey14/OpenAI-Dall.E-Image-Generation-in-Python)._

## What's this?

It is a Python script to generate batch of images using OpenAI's DALL-E model. It also saves the output images and handles the cooldown time of the API.

## Requirements

- Python 3.8+
- `pip`

## Set Up

1. Install the required packages

   ```bash
   pip install -r requirements.txt
   ```

2. Copy example files

   ```bash
   cp prompt.txt.example prompt.txt
   cp.env.example .env
   ```

3. Edit `.env` file and set the API key from [OpenAI](https://platform.openai.com/api-keys)

   ```bash
   vim .env
   ```

## Usage

1. Edit `prompt.txt` file and set the prompt (each line is a separate prompt)

   ```bash
   vim prompt.txt
   ```

2. Run the script

   ```bash
   python dalle.py
   ```

3. The output images will be saved in the `output` directory
