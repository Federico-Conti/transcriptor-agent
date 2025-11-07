
# 🎧 Transcriptor Agent

**Transform audio files into organized, topic-structured markdown documents using Azure OpenAI**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-orange.svg)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

## Features

- 🎵 **Audio Transcription**: Convert audio files to text using Azure OpenAI's transcription models
- 📋 **Smart Processing**: Automatically organize transcriptions into topic-based sections
- 🔄 **Batch Processing**: Handle large audio files by chunking them automatically
- 📁 **Flexible Output**: Generate both raw transcriptions and structured markdown documents

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI account with access to:
    - Audio transcription model (e.g., `gpt-4o-mini-transcribe`, `gpt-4o-transcribe`, `gpt-4o-transcribe-diarize`)
    - GPT completion model (e.g., `gpt-5`, `gpt-5-mini` or Legacy models)

### Installation

1. **Clone and setup environment**:
   
     ```bash
     git clone <repository-url>
     cd transcriptor-agent
     source ./start.sh  # Creates virtual environment and installs dependencies
     ```

2. **Configure environment variables**:
   
     ```markdown
     Create a `.env` file in the project root with the following variables:

     ```sh
     AZURE_OPENAI_KEY="your_api_key"
     # The API key for authenticating requests to your Azure OpenAI resource.

     AZURE_OPENAI_ENDPOINT="https://...azure.com/"
     # The base URL of your Azure OpenAI resource.

     AZURE_OPENAI_STT_ENDPOINT="https://.../audio/transcriptions?api-version=..."
     # The endpoint URL for the Azure OpenAI audio transcription service.

     AZURE_OPENAI_STT_MODEL="transcription_model_name"
     # The name of the deployed Azure OpenAI transcription model.

     AZURE_OPENAI_COMPLETION_MODEL="gpt_model_name"
     # The name of the deployed Azure OpenAI completion model.

     AZURE_OPENAI_API_VERSION="2024-12-01-preview"
     # The API version to use for the Azure OpenAI completion model.

     INPUT_FOLDER="/path/to/your/audio"
     # The directory path where input audio files are stored.

     OUTPUT_FOLDER="/path/to/output"
     # The directory path where output files will be saved.

     EXTENSION_OUTPUT_TRANSCRIPTION=".md"
     # The file extension for transcription output (e.g., .md, .txt).

     CHUNK_LENGTH_MS="300000"
     # The length of audio chunks in milliseconds (e.g., 300000 for 5 minutes).
     ```
   
## Usage

### Complete Workflow

Process audio file from transcription to organized markdown:
```bash
python app.py filename.mp3
```

**Output**:

- `filename.md` → Raw transcription
- `filename_withTopics.md` → Organized with topic sections

### Individual Components

**Transcription only**:
```bash
python transcriptor.py filename.mp3
```

**Process existing transcription**:
```bash
python process.py filename.md
```

## 📂 Project Structure

```
transcriptor-agent/
├── app.py              # Main orchestrator script
├── transcriptor.py     # Audio transcription module
├── process.py          # Transcription processing module
├── transcriptor.sh     # Shell script for only audio transcription
├── requirements.txt    # Python dependencies
├── start.sh            # Environment setup script
```
     
## ⚠️ Important Notes

- **Audio Limits**: Azure OpenAI audio models support approximately 20 minutes per request
- **Chunking**: Large files are automatically split into manageable chunks
- **Output Location**: All files are saved to the directory specified in `OUTPUT_FOLDER` env variable
- **Supported Formats**: `.mp3`, `.m4a`, and other common audio formats

