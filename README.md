# Bengali Text-to-Speech (TTS) Model

This project converts Bengali text into Bengali speech using Bengali neural TTS
voices.

```text
Bengali text -> Bengali neural TTS voice -> MP3 audio
```

## Project Structure

```text
Language Model/
  data/bengali/          # Bengali audio files and transcriptions
  models/                # Dataset report and model/cache files
  output/                # Generated Bengali speech files
  src/
    01_quick_test.py     # Quick Bengali neural TTS test
    02_data_preparation.py
    03_finetune_model.py # Dataset readiness report
    04_inference.py      # Main Bengali TTS inference script
```

## Install

```powershell
.\.venv311\Scripts\python.exe -m pip install -r requirements_phase1.txt
```

## Generate Bengali Speech

```powershell
.\.venv311\Scripts\python.exe src\04_inference.py --text "আমি বাংলা ভালোবাসি।" --output output\submission_bengali.mp3
```

Male voice:

```powershell
.\.venv311\Scripts\python.exe src\04_inference.py --voice male_bd --text "আমি বাংলা ভালোবাসি।" --output output\male_voice.mp3
```

List voices:

```powershell
.\.venv311\Scripts\python.exe src\04_inference.py --list-voices
```

## Dataset

Use one short sentence per audio file:

```text
data/bengali/audio_001.wav
data/bengali/audio_001.txt
```

The `.txt` file must contain the exact Bengali sentence spoken in the `.wav`.

Prepare metadata:

```powershell
.\.venv311\Scripts\python.exe src\02_data_preparation.py
```

Create the dataset report:

```powershell
.\.venv311\Scripts\python.exe src\03_finetune_model.py
```
