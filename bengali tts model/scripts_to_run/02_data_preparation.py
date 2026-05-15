"""
Data preparation for Bengali TTS fine-tuning.

Expected structure:
    data/bengali/audio_001.wav
    data/bengali/audio_001.txt

Each .txt file must contain the exact Bengali words spoken in the matching
.wav file.
"""

import csv
import sys
import wave
from pathlib import Path
from typing import Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class DataPreparer:
    """Prepares Bengali audio/text pairs for TTS fine-tuning."""

    def __init__(self, data_dir: str | Path):
        self.data_dir = Path(data_dir)
        self.bengali_dir = self.data_dir / "bengali"

    def validate_audio_file(self, filepath: str | Path) -> Tuple[bool, str]:
        """Validate a WAV audio file."""
        try:
            with wave.open(str(filepath), "rb") as wav_file:
                frames = wav_file.getnframes()
                rate = wav_file.getframerate()
                channels = wav_file.getnchannels()
                duration = frames / rate

                if duration < 1:
                    return False, f"too short: {duration:.1f}s (minimum 1s)"
                if duration > 30:
                    return False, f"too long: {duration:.1f}s (keep clips under 30s)"
                if rate not in [16000, 22050, 44100, 48000]:
                    return False, f"unsupported sample rate: {rate}Hz"
                if channels not in [1, 2]:
                    return False, f"unsupported channel count: {channels}"

                return True, f"valid ({duration:.1f}s, {rate}Hz, {channels} channel(s))"
        except Exception as exc:
            return False, str(exc)

    def create_metadata_csv(self) -> list[list[str]]:
        """Create data/bengali/metadata.csv in format: audio_file|text."""
        print("\nCreating metadata for Bengali...")

        self.bengali_dir.mkdir(exist_ok=True, parents=True)
        metadata = []
        wav_files = sorted(self.bengali_dir.glob("*.wav"))

        if not wav_files:
            print(f"No .wav files found in {self.bengali_dir}")
            print("Example expected file: audio_001.wav with audio_001.txt")
            return metadata

        for wav_file in wav_files:
            txt_file = wav_file.with_suffix(".txt")

            if not txt_file.exists():
                print(f"WARNING missing transcription: {txt_file.name}")
                continue

            is_valid, message = self.validate_audio_file(wav_file)
            if not is_valid:
                print(f"SKIP {wav_file.name}: {message}")
                continue

            text = txt_file.read_text(encoding="utf-8").strip()
            if not text:
                print(f"WARNING empty transcription: {txt_file.name}")
                continue

            metadata.append([wav_file.name, text])
            print(f"OK {wav_file.name}: {text[:60]}")

        output_path = self.bengali_dir / "metadata.csv"
        with output_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerows(metadata)

        print(f"\nCreated: {output_path} ({len(metadata)} entries)")
        return metadata

    def verify_data_structure(self):
        """Show current Bengali training-data status."""
        print("Verifying Bengali data structure...")

        self.bengali_dir.mkdir(exist_ok=True, parents=True)
        wav_count = len(list(self.bengali_dir.glob("*.wav")))
        txt_count = len(list(self.bengali_dir.glob("*.txt")))
        print(f"  {self.bengali_dir}: {wav_count} audio files, {txt_count} text files")

    def show_sample_sentences(self):
        """Print starter Bengali sentences you can record."""
        bengali_samples = [
            ("আমার নাম রহিম।", "My name is Rahim."),
            ("আপনি কীভাবে আছেন?", "How are you?"),
            ("এটি একটি নমুনা বাক্য।", "This is a sample sentence."),
            ("বাংলা ভাষা খুবই সুন্দর।", "Bengali language is very beautiful."),
            ("কৃত্রিম বুদ্ধিমত্তা ভবিষ্যতের প্রযুক্তি।", "AI is a technology of the future."),
        ]

        print("\nSample Bengali sentences:")
        for text, english in bengali_samples:
            print(f"  {text} ({english})")

        print("\nRecord each sentence as a separate WAV file.")
        print("Example: data/bengali/audio_001.wav and data/bengali/audio_001.txt")


if __name__ == "__main__":
    preparer = DataPreparer(PROJECT_ROOT / "data")

    print("=" * 60)
    print("Bengali TTS Data Preparation Tool")
    print("=" * 60)

    preparer.verify_data_structure()
    preparer.show_sample_sentences()
    preparer.create_metadata_csv()

    print("\n" + "=" * 60)
    print("Beginner checklist:")
    print("1. Record clean Bengali WAV clips, one sentence per file.")
    print("2. Save matching UTF-8 Bengali text files with the exact spoken words.")
    print("3. Run this script again to create metadata.csv.")
    print("=" * 60)
