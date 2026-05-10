"""
Bengali Text-to-Speech inference.

The default engine uses Microsoft Edge neural Bengali voices through edge-tts.
It produces Bengali MP3 output directly from Bengali text.
"""

import argparse
import asyncio
import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_EDGE_VOICE = "bn-BD-NabanitaNeural"
EDGE_BENGALI_VOICES = {
    "female_bd": "bn-BD-NabanitaNeural",
    "male_bd": "bn-BD-PradeepNeural",
    "female_in": "bn-IN-TanishaaNeural",
    "male_in": "bn-IN-BashkarNeural",
}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


class BengaliTTS:
    """Generate Bengali speech using a neural Bengali voice."""

    def __init__(self, engine: str = "edge", voice: str = DEFAULT_EDGE_VOICE):
        self.engine = engine
        self.voice = EDGE_BENGALI_VOICES.get(voice, voice)
        self.lang_code = "bn"

    async def _generate_edge_async(self, text: str, output_file: Path) -> bool:
        try:
            import edge_tts
        except ImportError:
            print("ERROR: edge-tts is not installed. Run: pip install edge-tts")
            return False

        print(f"\nGenerating Bengali neural speech with {self.voice}...")
        communicate = edge_tts.Communicate(text=text, voice=self.voice)
        await communicate.save(str(output_file))
        print(f"OK saved: {output_file}")
        return True

    def _generate_edge(self, text: str, output_file: Path) -> bool:
        return asyncio.run(self._generate_edge_async(text, output_file))

    def _generate_gtts(self, text: str, output_file: Path) -> bool:
        try:
            from gtts import gTTS
        except ImportError:
            print("ERROR: gTTS is not installed. Run: pip install gTTS")
            return False

        print("\nGenerating Bengali speech with gTTS...")
        gTTS(text=text, lang=self.lang_code, slow=False).save(str(output_file))
        print(f"OK saved: {output_file}")
        return True

    def generate(self, text: str, output_file: str | Path) -> bool:
        output_path = Path(output_file)
        output_path.parent.mkdir(exist_ok=True, parents=True)

        if self.engine == "edge":
            return self._generate_edge(text, output_path)
        if self.engine == "gtts":
            return self._generate_gtts(text, output_path)

        print(f"ERROR: Unknown engine: {self.engine}")
        return False


def batch_generate(input_file: str | Path, output_dir: str | Path, engine: str, voice: str) -> bool:
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        return False

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)
    texts = [line.strip() for line in input_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    print(f"Found {len(texts)} Bengali texts to process")
    tts = BengaliTTS(engine=engine, voice=voice)

    success = True
    for index, text in enumerate(texts, 1):
        filename = output_path / f"bengali_{index:03d}.mp3"
        success = tts.generate(text, filename) and success
    return success


def interactive_mode(engine: str, voice: str) -> None:
    print("\n" + "=" * 60)
    print("Interactive Bengali Text-to-Speech")
    print("=" * 60)

    tts = BengaliTTS(engine=engine, voice=voice)

    while True:
        text = input("\nEnter Bengali text (or 'quit' to exit):\n> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            print("Please enter Bengali text.")
            continue

        output_file = OUTPUT_DIR / f"bengali_{abs(hash(text)) % 10000}.mp3"
        tts.generate(text, output_file)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Bengali speech from Bengali text")
    parser.add_argument("--text", help="Bengali text to convert to speech")
    parser.add_argument("--output", help="Output MP3 file path")
    parser.add_argument("--engine", choices=["edge", "gtts"], default="edge", help="TTS engine")
    parser.add_argument(
        "--voice",
        default=DEFAULT_EDGE_VOICE,
        help=(
            "Edge voice name or alias: female_bd, male_bd, female_in, male_in, "
            "bn-BD-NabanitaNeural, bn-BD-PradeepNeural"
        ),
    )
    parser.add_argument("--interactive", action="store_true", help="Run interactive mode")
    parser.add_argument("--batch", help="UTF-8 text file with one Bengali sentence per line")
    parser.add_argument("--batch-output", default=str(OUTPUT_DIR), help="Batch output directory")
    parser.add_argument("--list-voices", action="store_true", help="Show supported Bengali voices")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list_voices:
        print("Supported Bengali Edge neural voices:")
        for alias, voice in EDGE_BENGALI_VOICES.items():
            print(f"  {alias}: {voice}")
        return 0

    if args.interactive:
        interactive_mode(engine=args.engine, voice=args.voice)
        return 0

    if args.batch:
        return 0 if batch_generate(args.batch, args.batch_output, args.engine, args.voice) else 1

    if args.text and args.output:
        tts = BengaliTTS(engine=args.engine, voice=args.voice)
        return 0 if tts.generate(args.text, args.output) else 1

    print("\nBengali TTS examples:")
    print("  python src\\04_inference.py --list-voices")
    print("  python src\\04_inference.py --text \"আমি বাংলা ভালোবাসি।\" --output output\\submission_bengali.mp3")
    print(
        "  python src\\04_inference.py --voice male_bd "
        "--text \"আমি বাংলা ভালোবাসি।\" --output output\\male_voice.mp3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
