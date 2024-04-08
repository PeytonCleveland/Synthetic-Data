import os
import argparse
from synthetic_data.settings import settings
import json
import asyncio
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate book titles from a given subject.")
    parser.add_argument("subject", help="Input subject", type=str)
    parser.add_argument("-o", "--out", default="titles.json", help="Output filename (flat json list), defaults to titles.json", type=str, nargs='?')
    parser.add_argument("-n", "--number", default=10, help="Number of titles to generate", type=int, nargs='?')
    args = parser.parse_args()

    print(f"Generating {args.number} book titles for subject: '{args.subject}' and saving to {args.out}")

    # Generate titles
    titles = []
    for i in tqdm(range(args.number)):
        try:
            titles.append(asyncio.run(generate_titles(args.subject)))
        except Exception as error:
            print(f"Error generating titles: {error}")

    # Make output directory
    if not os.path.exists("output"):
        os.makedirs("output")

    # Save to file
    with open(os.path.join(settings.OUTPUT_DIR, args.out_file), 'w') as f:
        f.write("\n".join(titles))

    print("Done!")