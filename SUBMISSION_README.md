# Bengali Text-to-Speech Submission

## Project Goal

This project converts Bengali text into Bengali speech.

```text
Bengali text -> Bengali neural TTS voice -> MP3 audio output
```

## Working Model

The working TTS model path is implemented in:

```text
src/04_inference.py
```

It uses Microsoft Edge neural Bengali voices through the `edge-tts` Python
package. This gives natural Bengali speech and supports both Bangladesh and
India Bengali voices.

Default voice:

```text
bn-BD-NabanitaNeural
```

Available voice aliases:

```text
female_bd -> bn-BD-NabanitaNeural
male_bd   -> bn-BD-PradeepNeural
female_in -> bn-IN-TanishaaNeural
male_in   -> bn-IN-BashkarNeural
```

## Dataset

The project includes 20 Bengali WAV clips with matching Bengali text
transcriptions:

```text
data/bengali/audio_001.wav
data/bengali/audio_001.txt
...
data/bengali/audio_020.wav
data/bengali/audio_020.txt
```

The metadata file is:

```text
data/bengali/metadata.csv
```

Regenerate it with:

```powershell
.\.venv311\Scripts\python.exe src\02_data_preparation.py
```

Generate the dataset report with:

```powershell
.\.venv311\Scripts\python.exe src\03_finetune_model.py
```

## Generate Speech

Female Bengali voice:

```powershell
.\.venv311\Scripts\python.exe src\04_inference.py --voice female_bd --text "নমস্কার, এটি আমার বাংলা টেক্সট টু স্পিচ মডেলের চূড়ান্ত নমুনা।" --output output\final_bengali_tts_female.mp3
```

Male Bengali voice:

```powershell
.\.venv311\Scripts\python.exe src\04_inference.py --voice male_bd --text "নমস্কার, এটি আমার বাংলা টেক্সট টু স্পিচ মডেলের চূড়ান্ত নমুনা।" --output output\final_bengali_tts_male.mp3
```

## Final Output Files

```text
output/final_bengali_tts_female.mp3
output/final_bengali_tts_male.mp3
output/submission_bengali_female.mp3
output/submission_bengali_male.mp3
```

## Important Note

Coqui XTTS v2 was tested, but it does not support Bengali language code `bn`.
For this submission, the correct working Bengali neural TTS model path is Edge
neural Bengali TTS through `src/04_inference.py`.
