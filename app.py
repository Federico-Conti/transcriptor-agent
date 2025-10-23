import sys
from transcriptor import transcribe_audio
from process import process_transcript


def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <input_audio_filename>")
        sys.exit(1)

    input_audio = sys.argv[1]

    print(f"[STARTING] Processing audio file: {input_audio}")
    transcript_path = transcribe_audio(input_audio)

    transcript_filename = transcript_path.split("/")[-1]
    print(f"[STARTING] Processing transcript file: {transcript_filename}")

    # Step 3: Processa la trascrizione
    process_transcript(transcript_filename)

if __name__ == "__main__":
    main()
