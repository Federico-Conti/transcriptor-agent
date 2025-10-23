import os
import requests
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_STT_ENDPOINT")
MODEL = os.getenv("AZURE_OPENAI_STT_MODEL")
INPUT_FOLDER = os.getenv("INPUT_FOLDER")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER")
EXT = os.getenv("EXTENSION_OUTPUT_TRANSCRIPTION")
CHUNK_LENGTH_MS = int(os.getenv("CHUNK_LENGTH_MS"))

def transcribe_audio(input_filename: str) -> str:
    input_path = os.path.join(INPUT_FOLDER, input_filename)
    base_name, _ = os.path.splitext(input_filename)
    output_path = os.path.join(OUTPUT_FOLDER, base_name + EXT)

    audio = AudioSegment.from_file(input_path)
    chunks = [audio[i:i+CHUNK_LENGTH_MS] for i in range(0, len(audio), CHUNK_LENGTH_MS)]

    if os.path.exists(output_path):
        os.remove(output_path)

    for idx, chunk in enumerate(chunks):
        chunk_filename = f"chunk_{idx}.mp3"
        chunk.export(chunk_filename, format="mp3")

        print(f"[INFO] sended chunk {idx+1}/{len(chunks)}")

        with open(chunk_filename, "rb") as f:
            files = {
                "file": (chunk_filename, f, "audio/mpeg"),
            }
            data = {
                "model": MODEL
            }
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }

            response = requests.post(ENDPOINT, headers=headers, files=files, data=data)

            if response.status_code == 200:
                text = response.json()["text"]
                with open(output_path, "a", encoding="utf-8") as out:
                    out.write(text + "\n")
            else:
                print(f"[ERROR] Chunk {idx+1}: {response.status_code} - {response.text}")

        os.remove(chunk_filename)

    print(f"✅ Transcript saved to {output_path}")
    return output_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python transcriptor.py <input_filename>")
        sys.exit(1)

    transcribe_audio(sys.argv[1])
