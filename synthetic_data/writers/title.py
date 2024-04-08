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
    pass


def generate_title(
    subject: str,
) -> List[str]:
    pass
