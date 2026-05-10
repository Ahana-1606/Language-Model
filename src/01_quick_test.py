"""
Quick Bengali TTS test.

Run this first to create a Bengali MP3 with the default neural Bengali voice.
"""

import asyncio
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

BENGALI_SAMPLE = "নমস্কার, আমি একটি বাংলা টেক্সট টু স্পিচ মডেল পরীক্ষা করছি।"
EDGE_VOICE = "bn-BD-NabanitaNeural"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


async def generate_edge_sample() -> bool:
    try:
        import edge_tts
    except ImportError:
        print("ERROR: edge-tts is not installed. Run: pip install edge-tts")
        return False

    output_file = OUTPUT_DIR / "bengali_neural_test.mp3"
    communicate = edge_tts.Communicate(text=BENGALI_SAMPLE, voice=EDGE_VOICE)
    await communicate.save(str(output_file))
    print(f"OK Bengali neural TTS saved: {output_file}")
    return True


def main() -> int:
    print("=" * 60)
    print("Bengali Neural TTS Quick Test")
    print("=" * 60)
    return 0 if asyncio.run(generate_edge_sample()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
