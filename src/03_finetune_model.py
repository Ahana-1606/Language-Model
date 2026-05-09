"""
Fine-tuning placeholder for a Bengali Text-to-Speech model.

Real fine-tuning needs Python 3.10/3.11, a GPU for practical training, and a
clean Bengali dataset. Use this script after data/bengali/metadata.csv exists.
"""

import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BENGALI_SAMPLE = "আমি একটি কৃত্রিম বুদ্ধিমত্তা ভিত্তিক বাংলা টেক্সট টু স্পিচ মডেল পরীক্ষা করছি।"


def check_bengali_dataset(data_dir: str) -> int:
    """Check whether the Bengali dataset is ready for a tiny experiment."""
    data_path = Path(data_dir)
    metadata_file = data_path / "bengali" / "metadata.csv"

    if not metadata_file.exists():
        print(f"\nERROR: Metadata file not found: {metadata_file}")
        print("Create it first with: python src\\02_data_preparation.py")
        return 0

    rows = [line for line in metadata_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"Dataset ready: {len(rows)} Bengali clips found in metadata.csv")

    if len(rows) < 20:
        print("WARNING: Fewer than 20 clips. Record more before experimenting.")
    elif len(rows) < 50:
        print("Tiny experiment mode: 20 clips is enough to test the pipeline, not enough for a good voice.")
    else:
        print("Good beginner dataset size for a first fine-tuning attempt.")

    return len(rows)


def finetune_tts(data_dir: str, output_dir: str):
    """Load a pre-trained TTS model and confirm Bengali data is ready."""
    print("\n" + "=" * 60)
    print("Bengali TTS Fine-Tuning Check")
    print("=" * 60)

    num_samples = check_bengali_dataset(data_dir)
    if num_samples == 0:
        return

    try:
        from TTS.api import TTS
    except ImportError:
        print("ERROR: Coqui TTS is not installed.")
        print("For full fine-tuning, use Python 3.10 or 3.11, then run: pip install TTS")
        print("\nYour 20-clip Bengali dataset is prepared, but this computer is not ready for model fine-tuning yet.")
        return

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    print("\nLoading pre-trained model for a sample Bengali generation...")
    try:
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
        sample_output = output_path / "bengali_sample.wav"
        tts.tts_to_file(text=BENGALI_SAMPLE, file_path=str(sample_output), language="bn")
        print(f"OK generated sample: {sample_output}")
    except Exception as exc:
        print(f"ERROR: Model test failed: {exc}")
        return

    print("\nNext step: use a full Coqui training recipe once your Bengali dataset is large enough.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fine-tune a Bengali TTS model")
    parser.add_argument("--data-dir", default=str(PROJECT_ROOT / "data"), help="Path to data directory")
    parser.add_argument("--output-dir", default=str(PROJECT_ROOT / "models"), help="Path to save model/output")
    args = parser.parse_args()

    finetune_tts(data_dir=args.data_dir, output_dir=args.output_dir)
