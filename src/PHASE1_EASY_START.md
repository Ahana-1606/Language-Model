# Phase 1: Easy Bengali TTS

Use an existing TTS engine first. This proves that Bengali text-to-speech works
before you collect data or train anything.

## gTTS

```python
from gtts import gTTS

text = "আমি বাংলা ভাষায় কথা বলছি।"
tts = gTTS(text=text, lang="bn", slow=False)
tts.save("bengali_speech.mp3")
```

Pros:

- easiest beginner option
- good enough for demos
- supports Bengali

Cons:

- needs internet
- not your own voice/model

## Local Windows Voice

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("আমি বাংলা ভাষায় কথা বলছি।")
engine.runAndWait()
```

Quality depends on the voices installed on your computer.
