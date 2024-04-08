import argparse
from synthetic_data.settings import settings
import json
import os
from synthetic_data.writers.outline import generate_outline
from tqdm import tqdm


def load_processed_titles(file_name: str):
    with open(os.path.join(settings.OUTPUT_DIR, file_name)) as f:
        titles = json.load(f)
    return titles["json"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate textbook outlines from titles."
    )
    parser.add_argument("in_file", help="Input filename (.json)")
    parser.add_argument(
        "-o",
        "--out",
        help="Output filename (.json)",
        type=str,
        default="outlines.json",
        nargs="?",
    )
    parser.add_argument(
        "-m",
        "--max",
        help="Maximum number of sections per outline",
        type=int,
        default=10,
        nargs="?",
    )
    args = parser.parse_args()

    titles = load_processed_titles(args.in_file)

    print(f"Generating outlines from {args.in_file} and saving to {args.out}")

    # Generate outlines
    outlines = []
