import json
import os
from typing import List, OrderedDict
from json import JSONDecodeError

from synthetic_data.llm.llm import get_llm
from synthetic_data.llm.parameters import Parameters
from synthetic_data.llm.prompt import create_prompt
from synthetic_data.settings import settings
from synthetic_data.util import extract_only_json_list


def title_prompt(subject: str) -> str:
    with open(os.path.join(settings.EXAMPLE_JSON_DIR, f"titles.json")) as file:
        examples = json.load(file)
    input = OrderedDict([("subject", subject)])
    prompt = create_prompt("title", input, examples)
    return prompt


def generate_title(
    subject: str,
) -> List[str]:
    prompt = title_prompt(subject)
    llm = get_llm(
        params=Parameters(temperature=0.95, max_tokens=200, frequency_penalty=0.5)
    )
    response = llm.complete(prompt, True)

    try:
        text = extract_only_json_list(response.text)
        data = json.loads(text.strip())
    except (JSONDecodeError, IndexError) as error:
        raise ValueError(f"Error generating title: {response.text}") from error
    return data
