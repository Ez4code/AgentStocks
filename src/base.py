from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for all LLM backends.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def chat(self, prompt: str, **kwargs) -> str:
        """
        Unified chat interface.
        """
        pass
