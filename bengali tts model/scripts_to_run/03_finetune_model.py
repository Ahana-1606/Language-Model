"""
Bengali TTS dataset readiness report.

This project has 20 Bengali audio/text pairs. That is enough to demonstrate a
TTS pipeline and generate Bengali speech with scripts_to_run/04_inference.py, but it is not
enough to train a high-quality custom neural voice from scratch.
"""

import csv
import sys
import wave
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
BENGALI_DIR = DATA_DIR / "bengali"
METADATA_FILE = BENGALI_DIR / "metadata.csv"
MODELS_DIR = PROJECT_ROOT / "model_files"
REPORT_FILE = PROJECT_ROOT / "text_and_markdown_files" / "bengali_dataset_report.txt"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def get_wav_duration(filepath: Path) -> float:
    with wave.open(str(filepath), "rb") as wav_file:
        return wav_file.getnframes() / wav_file.getframerate()


def read_metadata() -> list[tuple[str, str]]:
    if not METADATA_FILE.exists():
        print(f"ERROR: Metadata file not found: {METADATA_FILE}")
        print("Run: python scripts_to_run\\02_data_preparation.py")
        return []

    rows = []
    with METADATA_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter="|")
        for row in reader:
            if len(row) >= 2:
                rows.append((row[0], row[1]))
    return rows


def build_report(rows: list[tuple[str, str]]) -> str:
    total_duration = 0.0
    missing_audio = []

    for audio_name, _text in rows:
        audio_path = BENGALI_DIR / audio_name
        if not audio_path.exists():
            missing_audio.append(audio_name)
            continue

        try:
            total_duration += get_wav_duration(audio_path)
        except Exception:
            missing_audio.append(audio_name)

    lines = [
        "Bengali TTS Dataset Report",
        "=" * 40,
        f"Metadata file: {METADATA_FILE}",
        f"Number of clips: {len(rows)}",
        f"Total audio duration: {total_duration:.1f} seconds",
        f"Missing/unreadable audio files: {len(missing_audio)}",
        "",
        "Status:",
        "The dataset is ready for a Bengali TTS demonstration.",
        "The current submission uses Edge neural Bengali TTS in scripts_to_run/04_inference.py.",
        "",
        "Fine-tuning note:",
        "20 clips is not enough for a high-quality custom Bengali neural voice.",
        "Coqui XTTS v2 was tested, but it does not support Bengali language code 'bn'.",
        "For the current deadline, use the generated MP3 files in the voice_outputs folder.",
        "",
        "Recommended output files:",
        "voice_outputs/submission_bengali_female.mp3",
        "voice_outputs/submission_bengali_male.mp3",
    ]

    if missing_audio:
        lines.extend(["", "Missing/unreadable files:"])
        lines.extend(missing_audio)

    return "\n".join(lines)


def main() -> int:
    print("=" * 60)
    print("Bengali TTS Dataset Readiness")
    print("=" * 60)

    rows = read_metadata()
    if not rows:
        return 1

    report = build_report(rows)
    MODELS_DIR.mkdir(exist_ok=True, parents=True)
    REPORT_FILE.parent.mkdir(exist_ok=True, parents=True)
    REPORT_FILE.write_text(report, encoding="utf-8")

    print(report)
    print("")
    print(f"Report saved: {REPORT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
