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
    for title in tqdm(titles):
        try:
            outline = generate_outline(title, args.max)
            outlines.append(outline)
        except Exception as error:
            print(f"Error generating outline for {title}: {error}")

    # Make output directory
    output_path = os.path.join(settings.OUTPUT_DIR, args.out)
    if not os.path.exists(settings.OUTPUT_DIR):
        os.makedirs(settings.OUTPUT_DIR)

    # Save to file
    with open(output_path, "w") as f:
        json.dump(outlines, f, indent=2)

    print(f"Saving outlines to {args.out}")
