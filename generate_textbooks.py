import argparse
from synthetic_data.settings import settings
import json
import os
from synthetic_data.writers.outline import generate_outline
from synthetic_data.util import exact_deduplicate
from tqdm import tqdm


def load_processed_titles(file_name: str):
    with open(os.path.join(settings.OUTPUT_DIR, file_name)) as f:
        titles = json.load(f)
    return titles["json"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate textbooks from outlines, and dedupe."
    )
    parser.add_argument("in_file", help="Input filename (.json)")
    parser.add_argument(
        "-o",
        "--out",
        help="Output filename (.json)",
        type=str,
        default="textbooks.json",
        nargs="?",
    )
    parser.add_argument(
        "-m",
        "--max",
        help="Maximum number of sections per outline",
        type=int,
        default=15,
        nargs="?",
    )
    args = parser.parse_args()
