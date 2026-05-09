# Troubleshooting Bengali TTS

## Package Install Fails

If `pip install -r requirements.txt` fails, use the beginner file first:

```powershell
pip install -r requirements_phase1.txt
```

Your Python 3.13 setup can run Phase 1, but full AI fine-tuning is easier with
Python 3.10 or 3.11.

## No Bengali Audio File

Check:

- you are in `C:\Users\KIIT\Desktop\Language Model`
- you ran `python src\01_quick_test.py`
- the `output/` folder exists
- internet is working for `gTTS`

## Data Preparation Finds No Files

Your files must be here:

```text
data/bengali/audio_001.wav
data/bengali/audio_001.txt
```

The `.txt` file must contain the exact Bengali sentence spoken in the `.wav`.

## Audio Clip Rejected

Common reasons:

- clip is shorter than 1 second
- clip is longer than 30 seconds
- file is not WAV
- sample rate is unusual

Keep clips short, clean, and simple.

## Bengali Text Looks Broken

Make sure files are saved as UTF-8. Bengali should look like this:

```text
বাংলা ভাষা খুবই সুন্দর।
```
