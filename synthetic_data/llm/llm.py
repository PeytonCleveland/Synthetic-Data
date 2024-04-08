from llama_index.llms.openai import OpenAI
from synthetic_data.llm.parameters import Parameters


def get_llm(params=None) -> OpenAI:
    if params is None:
        params = Parameters()

    return OpenAI(
        model=params.model,
        api_key=params.api_key,
        temperature=params.temperature,
        max_tokens=params.max_tokens,
        frequency_penalty=params.frequency_penalty,
    )
