import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.getenv("AZURE_OPENAI_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_COMPLETION_MODEL")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER")

client = AzureOpenAI(
    api_key=subscription_key,
    api_version=api_version,
    azure_endpoint=endpoint,
)

system_prompt = """This is a English transcript of the master course I am taking.
Please maintain as much lexical fidelity and the structure of the original sentences as possible.
Segment the content into coherent thematic sections (topics), following the chronological order of the topics covered by the professor.
Each topic should have a concise and descriptive title starting with '## ' or '### ' depending on the level of the topic."""

def process_transcript(input_filename: str) -> str:
    input_path = os.path.join(OUTPUT_FOLDER, input_filename)

    with open(input_path, 'r', encoding='utf-8') as f:
        transcript = f.read()

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript},
        ]
    )

    output_markdown = response.choices[0].message.content
    base_name, _ = os.path.splitext(input_filename)
    output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_withTopics.md")

    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(output_markdown)

    print(f"✅ Transcript with topics saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python process.py <transcript_filename>")
        sys.exit(1)

    process_transcript(sys.argv[1])
    

   
