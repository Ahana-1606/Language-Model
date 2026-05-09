# Bengali TTS Workflow

Follow this order.

## Phase 1: Generate Bengali Speech

Install the small beginner dependency set:

```powershell
pip install -r requirements_phase1.txt
```

Run:

```powershell
python src\01_quick_test.py
```

Result: you can generate basic Bengali speech.

## Phase 2: Collect Bengali Data

Record short Bengali clips:

- 1 to 10 seconds each
- quiet room
- one sentence per clip
- same speaker if possible
- exact Bengali transcript for every clip

Folder format:

```text
data/
  bengali/
    audio_001.wav
    audio_001.txt
    audio_002.wav
    audio_002.txt
```

## Phase 3: Prepare Metadata

Run:

```powershell
python src\02_data_preparation.py
```

This creates:

```text
data/bengali/metadata.csv
```

## Phase 4: Fine-Tune Later

Fine-tuning needs:

- Python 3.10 or 3.11
- a GPU for practical training
- at least 50-100 clips for experiments
- many hours of clean audio for a good custom voice

Use:

```powershell
python src\03_finetune_model.py
```

## Phase 5: Generate Bengali Speech

```powershell
python src\04_inference.py --interactive
```

or:

```powershell
python src\04_inference.py --text "বাংলা ভাষা খুবই সুন্দর।" --output output\bengali_sentence.mp3
```
