#!/usr/bin/env bash
set -euo pipefail

# Required environment variables:
# AZURE_OPENAI_STT_ENDPOINT      - e.g. https://<your-resource>.openai.azure.com
# AZURE_OPENAI_KEY           - API key (do not print it)
# AZURE_OPENAI_STT_MODEL    - deployment name (e.g. ict-test_gpt4otranscribe)
# INPUT_FILE                 - path to the audio file to send
# OUTPUT_FILE                - output file (default: trascrizione.json)
# API_VERSION                - API version (default: 2025-03-01-preview)

: "${AZURE_OPENAI_STT_ENDPOINT:?AZURE_OPENAI_STT_ENDPOINT not set}"
: "${AZURE_OPENAI_KEY:?AZURE_OPENAI_KEY not set}"
: "${AZURE_OPENAI_STT_MODEL:?AZURE_OPENAI_STT_MODEL not set}"
: "${INPUT_FILE:?INPUT_FILE not set}"
OUTPUT_FILE="${OUTPUT_FILE:-trascrizione.json}"


if [[ ! -f "$INPUT_FILE" ]]; then
  echo "Error: input file not found: $INPUT_FILE" >&2
  exit 2
fi



# Execute the request (do not print the key)
curl -X POST $AZURE_OPENAI_STT_ENDPOINT \
  -H "Authorization: Bearer $AZURE_OPENAI_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@${INPUT_FILE}" \
  -F "model=${AZURE_OPENAI_STT_MODEL}" \
  --progress-bar \
  > "$OUTPUT_FILE"

echo "Transcription saved to: $OUTPUT_FILE"
