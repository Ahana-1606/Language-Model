# Phase 2: Bengali Fine-Tuning

Fine-tuning means taking an existing TTS model and adjusting it with your own
Bengali audio/text data.

## Data Needed

For experiments:

- 50-100 Bengali clips
- 1 to 10 seconds each
- exact Bengali transcript for every clip

For a useful custom voice:

- 5 to 20 hours of clean Bengali audio
- one consistent speaker if possible
- same microphone and recording setup

## Data Format

```text
data/bengali/audio_001.wav
data/bengali/audio_001.txt
data/bengali/audio_002.wav
data/bengali/audio_002.txt
```

Example `audio_001.txt`:

```text
বাংলা ভাষা খুবই সুন্দর।
```

## Prepare Metadata

```powershell
python src\02_data_preparation.py
```

This creates:

```text
data/bengali/metadata.csv
```

## Important

Your current Python 3.13 setup is fine for Phase 1. For full fine-tuning, use
Python 3.10 or 3.11 because many AI audio libraries do not support Python 3.13
yet.
