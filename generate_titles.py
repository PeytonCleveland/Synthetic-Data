import os
import argparse
from synthetic_data.settings import settings
from synthetic_data.writers.title import generate_title
from synthetic_data.util import exact_deduplicate
from synthetic_data.embeddings.embeddings import Embeddings
import json
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate book titles from a given subject.")
    parser.add_argument("subject", help="Input subject", type=str)
    parser.add_argument("-o", "--out", default="titles.json", help="Output filename (.json), defaults to titles.json", type=str, nargs='?')
    parser.add_argument("-i", "--iterations", default=5, help="Number of iterations", type=int, nargs='?')
    args = parser.parse_args()

    print(f"Generating book titles for subject: '{args.subject}' and saving to {args.out}")

    # Generate titles
    titles = []
    for i in tqdm(range(args.iterations)):
        try:
            new_titles = generate_title(args.subject)
            titles.extend(new_titles)
        except Exception as error:
            print(f"Error generating title: {error}")

    # Deduplicate
    titles = exact_deduplicate(titles)

    # Embeddings
    embeddings = Embeddings()
    embeddings.add_list(titles)
    embeddings.dedupe(threshold=0.75)
    titles = [title for title, _ in embeddings.get()]

    # Format
    titles = {
        "subject": args.subject,
        "json": titles 
    }

    # Make output directory
    if not os.path.exists(settings.OUTPUT_DIR):
        os.makedirs(settings.OUTPUT_DIR)

    # Save to file
    with open(os.path.join(settings.OUTPUT_DIR, args.out), 'w') as f:
        json.dump(titles, f, indent=2)

    print(f"Saving titles to {args.out}")