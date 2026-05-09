"""
Bengali Text-to-Speech inference.

Use this after Phase 1 to generate Bengali speech from your own text.
"""

import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"


class TTSInference:
    """Generate Bengali speech using gTTS or Coqui."""

    def __init__(self, engine: str = "gtts"):
        self.engine = engine
        self.lang_code = "bn"
        self.model = None

        if engine == "coqui":
            self._init_coqui()

    def _init_coqui(self):
        try:
            from TTS.api import TTS

            print("Loading Coqui TTS model for Bengali...")
            self.model = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
            print("OK Coqui TTS ready")
        except ImportError:
            print("ERROR: Coqui TTS not installed. Run: pip install TTS")

    def generate_speech_coqui(self, text: str, output_file: str):
        if not self.model:
            print("ERROR: Coqui model not initialized")
            return

        try:
            print(f"\nGenerating Bengali speech: {text[:50]}...")
            self.model.tts_to_file(text=text, file_path=output_file, language=self.lang_code)
            print(f"OK saved: {output_file}")
        except Exception as exc:
            print(f"ERROR: {exc}")

    def generate_speech_gtts(self, text: str, output_file: str):
        try:
            from gtts import gTTS

            print(f"\nGenerating Bengali speech: {text[:50]}...")
            gTTS(text=text, lang=self.lang_code, slow=False).save(output_file)
            print(f"OK saved: {output_file}")
        except ImportError:
            print("ERROR: gTTS not installed. Run: pip install gTTS")
        except Exception as exc:
            print(f"ERROR: {exc}")

    def generate_speech(self, text: str, output_file: str):
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        if self.engine == "coqui":
            self.generate_speech_coqui(text, output_file)
        elif self.engine == "gtts":
            self.generate_speech_gtts(text, output_file)
        else:
            print(f"ERROR: Unknown engine: {self.engine}")


def batch_generate(input_file: str, output_dir: str, engine: str = "gtts"):
    """Generate Bengali speech for each non-empty line in a UTF-8 text file."""
    if not os.path.exists(input_file):
        print(f"ERROR: Input file not found: {input_file}")
        return

    tts = TTSInference(engine=engine)

    with open(input_file, "r", encoding="utf-8") as file:
        texts = [line.strip() for line in file if line.strip()]

    print(f"Found {len(texts)} Bengali texts to process")

    os.makedirs(output_dir, exist_ok=True)
    for index, text in enumerate(texts, 1):
        extension = "wav" if engine == "coqui" else "mp3"
        output_file = os.path.join(output_dir, f"bengali_{index:03d}.{extension}")
        tts.generate_speech(text, output_file)


def interactive_mode(engine: str = "gtts"):
    """Interactive Bengali text-to-speech generator."""
    print("\n" + "=" * 60)
    print("Interactive Bengali Text-to-Speech")
    print("=" * 60)

    tts = TTSInference(engine=engine)

    while True:
        text = input("\nEnter Bengali text (or 'quit' to exit):\n> ").strip()

        if text.lower() == "quit":
            break

        if not text:
            print("Please enter some Bengali text")
            continue

        extension = "wav" if engine == "coqui" else "mp3"
        output_file = OUTPUT_DIR / f"bengali_{abs(hash(text)) % 10000}.{extension}"
        tts.generate_speech(text, str(output_file))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Bengali speech from text")
    parser.add_argument("--text", help="Bengali text to convert to speech")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--engine", choices=["gtts", "coqui"], default="gtts", help="TTS engine")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--batch", help="Batch mode: path to UTF-8 text file")
    parser.add_argument("--batch-output", default=str(OUTPUT_DIR), help="Batch output directory")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode(engine=args.engine)
    elif args.batch:
        batch_generate(args.batch, args.batch_output, engine=args.engine)
    elif args.text and args.output:
        TTSInference(engine=args.engine).generate_speech(args.text, args.output)
    else:
        print("\nBengali TTS examples:")
        print("  python src\\04_inference.py --interactive")
        print("  python src\\04_inference.py --text \"আমি বাংলা ভালোবাসি।\" --output output\\my_bengali.mp3")
