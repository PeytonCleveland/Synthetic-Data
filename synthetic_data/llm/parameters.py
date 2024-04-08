from synthetic_data.settings import settings


class Parameters:
    def __init__(
        self,
        model="gpt-4",
        temperature=0.8,
        max_tokens=512,
        frequency_penalty=0.0,
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty
        self.api_key = settings.OPENAI_API_KEY
