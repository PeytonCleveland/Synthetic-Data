import os
import re
import json
from collections import OrderedDict

from synthetic_data.llm.llm import get_llm
from synthetic_data.llm.parameters import Parameters
from synthetic_data.llm.prompt import create_prompt
from synthetic_data.settings import settings


def outline_prompt(title: str, max_chapters: int) -> str:
    with open(os.path.join(settings.EXAMPLE_JSON_DIR, "outlines.json")) as file:
        examples = json.load(file)
    input = OrderedDict([("title", title)])
    prompt = create_prompt("outline", input, examples, max_chapters=max_chapters)
    return prompt


def generate_outline(title: str, max_chapters: int) -> dict:
    prompt_text = outline_prompt(title, max_chapters)

    llm = get_llm(params=Parameters(temperature=0.95, max_tokens=4095))

    response = llm.complete(prompt_text, True)

    try:
        concepts_match = re.search(r"Concepts: (\[.*?\])", response.text)
        if concepts_match:
            concepts_list_str = concepts_match.group(1)
            concepts_list = json.loads(concepts_list_str.replace("'", '"'))
        else:
            raise ValueError("Concepts list not found in response")

        json_part = response.text.replace(concepts_match.group(0), "", 1).strip()

        outline_data = json.loads(json_part)

        structured_outline = {
            "title": title,
            "concepts": concepts_list,
            "outline": outline_data["outline"],
            "queries": outline_data.get("queries", []),
        }
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Failed to parse the LLM response for title '{title}': {error}")
        raise ValueError(f"Error generating outline: {response.text}") from error

    return structured_outline
