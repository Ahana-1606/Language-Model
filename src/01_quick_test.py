"""
Quick Test - Phase 1: Bengali Text-to-Speech.

Run this first. It creates Bengali speech without training a model.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

BENGALI_SAMPLE = "নমস্কার, আমি একটি বাংলা টেক্সট টু স্পিচ মডেল পরীক্ষা করছি।"


def test_gtts():
    """Best beginner option. Uses Google's TTS service, so it needs internet."""
    try:
        from gtts import gTTS

        output_file = OUTPUT_DIR / "bengali_gtts.mp3"
        gTTS(text=BENGALI_SAMPLE, lang="bn", slow=False).save(str(output_file))
        print(f"OK Bengali gTTS saved: {output_file}")

    except ImportError:
        print("ERROR: gTTS not installed. Run: pip install gTTS")
    except Exception as exc:
        print(f"ERROR: gTTS failed: {exc}")


def test_pyttsx3():
    """Offline fallback. Quality depends on the voices installed on Windows."""
    try:
        import pyttsx3

        output_file = OUTPUT_DIR / "bengali_pyttsx3.wav"

        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        engine.say(BENGALI_SAMPLE)
        engine.save_to_file(BENGALI_SAMPLE, str(output_file))
        engine.runAndWait()

        print(f"OK pyttsx3 Bengali played and saved: {output_file}")

    except ImportError:
        print("ERROR: pyttsx3 not installed. Run: pip install pyttsx3")
    except Exception as exc:
        print(f"ERROR: pyttsx3 failed: {exc}")


def test_coqui_tts():
    """AI model option. This is for later, after Python 3.10/3.11 setup."""
    try:
        from TTS.api import TTS

        output_file = OUTPUT_DIR / "bengali_coqui.wav"
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
        tts.tts_to_file(text=BENGALI_SAMPLE, file_path=str(output_file), language="bn")
        print(f"OK Coqui Bengali saved: {output_file}")

    except ImportError:
        print("INFO: Coqui TTS not installed yet. This is okay for Phase 1.")
    except Exception as exc:
        print(f"ERROR: Coqui TTS failed: {exc}")


if __name__ == "__main__":
    print("=" * 60)
    print("Phase 1 - Quick Bengali TTS Test")
    print("=" * 60)

    print("\n1. Testing gTTS:")
    print("-" * 60)
    test_gtts()

    print("\n2. Testing pyttsx3:")
    print("-" * 60)
    test_pyttsx3()

    print("\n3. Testing Coqui TTS:")
    print("-" * 60)
    test_coqui_tts()

    print("\n" + "=" * 60)
    print(f"Done. Check generated Bengali audio in: {OUTPUT_DIR}")
    print("=" * 60)
