import os
import argparse
from synthetic_data.settings import settings
from synthetic_data.writers.title import generate_title
from synthetic_data.util import exact_deduplicate
from synthetic_data.embeddings.embeddings import Embeddings
import json
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate book titles from a given subject."
    )
    parser.add_argument("subject", help="Input subject", type=str)
    parser.add_argument(
        "-o",
        "--out",
        default="titles.json",
        help="Output filename (.json), defaults to titles.json",
        type=str,
        nargs="?",
    )
    parser.add_argument(
        "-i",
        "--iterations",
        default=5,
        help="Number of iterations",
        type=int,
        nargs="?",
    )
    args = parser.parse_args()

    print(
        f"Generating book titles for subject: '{args.subject}' and saving to {args.out}"
    )

    # Generate titles
    titles = []
