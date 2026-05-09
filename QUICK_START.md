# Quick Start: Bengali TTS

## 1. Install Beginner Dependencies

```powershell
cd "C:\Users\KIIT\Desktop\Language Model"
pip install -r requirements_phase1.txt
```

## 2. Run The Bengali Test

```powershell
python src\01_quick_test.py
```

Check the `output/` folder. You should see files such as:

```text
bengali_gtts.mp3
bengali_pyttsx3.wav
```

## 3. Generate Your Own Bengali Speech

```powershell
python src\04_inference.py --text "আমি বাংলা ভালোবাসি।" --output output\my_bengali.mp3
```

## 4. Prepare For Custom Training

Record Bengali sentences and save them like this:

```text
data/bengali/audio_001.wav
data/bengali/audio_001.txt
```

Then run:

```powershell
python src\02_data_preparation.py
```
