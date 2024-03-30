import os
import time

import requests
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
n = int(os.getenv('N') or 5)
input_file = os.getenv('INPUT_FILE', 'prompt.txt')
target_dir = os.getenv('TARGET_DIRECTORY', 'outputs')
cooldown = int(os.getenv('COOLDOWN', 60))

if not api_key:
    raise ValueError('Api key not found in .env file')


def save_image_from_url(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), 'wb') as file:
        file.write(response.content)


client = OpenAI(api_key=api_key)

start_time = None
with open(input_file, 'r') as file:
    for line in file:
        if start_time:
            cooldown_time = cooldown - int(time.time() - start_time)
            print(f'Waiting {cooldown_time} sec for cooldown...')
            time.sleep(cooldown_time)

        prompt = line.strip()
        print(f'Generating images for prompt: {prompt}')

        start_time = time.time()
        response = client.images.generate(
            model='dall-e-2',
            prompt=prompt,
            size='1024x1024',
            quality='standard',
            n=n,
        )
        for i, image in enumerate(response.data):
            print(f'Downloading image {i + 1}/{n}...')
            save_image_from_url(image.url, f'{prompt.replace(" ", "_")}_{i + 1}.png')
