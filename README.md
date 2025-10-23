
# 🎧 Transcriptor Agent

**Transform audio files into organized, topic-structured markdown documents using Azure OpenAI**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-orange.svg)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)

## Features

- 🎵 **Audio Transcription**: Convert audio files to text using Azure OpenAI's transcription models
- 📋 **Smart Processing**: Automatically organize transcriptions into topic-based sections
- 🔄 **Batch Processing**: Handle large audio files by chunking them automatically
- 📁 **Flexible Output**: Generate both raw transcriptions and structured markdown documents

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure OpenAI account with access to:
    - Audio transcription model (e.g., `gpt-4o-audio-preview`)
    - GPT completion model (e.g., `GPT-4` or `GPT-3.5`)

### Installation

1. **Clone and setup environment**:
     ```bash
     git clone <repository-url>
     cd transcriptor-agent
     source ./start.sh  # Creates virtual environment and installs dependencies
     ```

2. **Configure environment variables**:
     Create a `.env` file in the project root:
     ```sh
     AZURE_OPENAI_KEY="your_api_key"
     AZURE_OPENAI_STT_ENDPOINT="https://.../audio/transcriptions?api-version=..."
     AZURE_OPENAI_ENDPOINT="https://...azure.com/"
     AZURE_OPENAI_STT_MODEL="transcription_model_name"
     AZURE_OPENAI_COMPLETION_MODEL="gpt_model_name"
     AZURE_OPENAI_API_VERSION="2024-12-01-preview"

     INPUT_FOLDER="/path/to/your/audio"
     OUTPUT_FOLDER="/path/to/output"
     EXTENSION_OUTPUT_TRANSCRIPTION=".md"
     CHUNK_LENGTH_MS="300000"  # 5 minutes in milliseconds
     ```

## 📖 Usage

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
├── requirements.txt    # Python dependencies
├── start.sh            # Environment setup script
```
     
## ⚠️ Important Notes

- **Audio Limits**: Azure OpenAI audio models support approximately 20 minutes per request
- **Chunking**: Large files are automatically split into manageable chunks
- **Output Location**: All files are saved to the directory specified in `OUTPUT_FOLDER` env variable
- **Supported Formats**: `.mp3`, `.m4a`, and other common audio formats

