# Beginner Roadmap: Bengali Text-to-Speech

You are building a Bengali text-to-speech system:

```text
written Bengali text -> TTS engine/model -> spoken Bengali audio
```

## What To Do First

Do not start by training a model from scratch. Start simple:

1. **Use an existing Bengali TTS engine**
   - Goal: prove your computer can generate Bengali speech.
   - File to run: `src/01_quick_test.py`
   - Best beginner engine: `gTTS`

2. **Collect clean Bengali data**
   - Goal: prepare your own voice or speaker data.
   - You need `.wav` audio and exact Bengali text transcripts.
   - File to run: `src/02_data_preparation.py`

3. **Fine-tune an existing model later**
   - Goal: make pronunciation and voice closer to your target.
   - File to study later: `src/03_finetune_model.py`
   - You should have at least a few hundred clean clips before this step.

4. **Generate Bengali speech**
   - Goal: type Bengali text and create speech files.
   - File to run: `src/04_inference.py`

## Minimum Data You Need

For experiments:

- 20 to 50 short Bengali clips
- 1 to 10 seconds per clip
- Quiet room
- Same speaker if possible
- Exact Bengali transcript for every clip

For a useful custom Bengali voice:

- 5 to 20 hours of clean audio
- Hundreds or thousands of clips
- Consistent microphone and speaking style

For training from scratch:

- Usually hundreds of hours
- Strong GPU
- Deep learning experience

## Folder Format

Use this structure:

```text
data/
  bengali/
    audio_001.wav
    audio_001.txt
    audio_002.wav
    audio_002.txt
```

Each `.txt` file must contain the exact Bengali sentence spoken in the matching
`.wav` file.

## Commands

Install beginner dependencies first:

```powershell
pip install -r requirements_phase1.txt
```

Run the first Bengali TTS test:

```powershell
python src\01_quick_test.py
```

Prepare training metadata:

```powershell
python src\02_data_preparation.py
```

Generate Bengali speech later:

```powershell
python src\04_inference.py --interactive
```

The full `requirements.txt` file is for later fine-tuning. If you have Python
3.13, some AI/audio packages may fail to install. For full model training, use
Python 3.10 or 3.11 in a virtual environment.

## Important Reality Check

If your goal is a project/demo, `gTTS` is enough to generate Bengali speech.

If your goal is a real custom Bengali voice, your main work is data collection.
The AI model matters, but clean audio plus exact Bengali text is what makes the
model good.
