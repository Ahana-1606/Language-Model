# Bengali Text-to-Speech (TTS) Model

This project is for building a Bengali text-to-speech system using AI tools.

Text-to-speech means:

```text
Bengali text -> TTS engine/model -> Bengali audio
```

## Project Structure

```text
Language Model/
  data/
    bengali/              # Bengali audio files and transcriptions
  models/                 # Saved trained models or model outputs
  output/                 # Generated Bengali speech files
  src/
    01_quick_test.py      # Run this first
    02_data_preparation.py
    03_finetune_model.py
    04_inference.py
  requirements_phase1.txt # Beginner dependencies
  requirements.txt        # Later fine-tuning dependencies
```

## Beginner Path

1. Run a quick Bengali TTS test.
2. Collect Bengali audio and matching Bengali text.
3. Prepare `metadata.csv`.
4. Fine-tune a model later when you have enough data.
5. Generate Bengali speech from your own text.

## First Commands

```powershell
pip install -r requirements_phase1.txt
python src\01_quick_test.py
```

Check the `output/` folder for Bengali audio files.

## Training Data Format

Use one short sentence per audio file:

```text
data/bengali/audio_001.wav
data/bengali/audio_001.txt
```

The `.txt` file must contain the exact Bengali sentence spoken in the `.wav`.
