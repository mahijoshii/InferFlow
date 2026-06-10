import re
from dataclasses import dataclass


@dataclass
class CacheEntry:
    prompt: str
    response: str
    selected_provider: str


class CacheService:
    def __init__(self, threshold: float = 0.75):
        self.threshold = threshold
        self.entries: list[CacheEntry] = []

    def find_match(self, prompt: str) -> CacheEntry | None:
        for entry in self.entries:
            if self._similarity(prompt, entry.prompt) >= self.threshold:
                return entry
        return None

    def add(self, prompt: str, response: str, selected_provider: str) -> None:
        self.entries.append(CacheEntry(prompt=prompt, response=response, selected_provider=selected_provider))

    def clear(self) -> None:
        self.entries.clear()

    def _similarity(self, first_text: str, second_text: str) -> float:
        first_words = self._words(first_text)
        second_words = self._words(second_text)
        if not first_words or not second_words:
            return 0

        shared_words = first_words.intersection(second_words)
        all_words = first_words.union(second_words)
        return len(shared_words) / len(all_words)

    def _words(self, text: str) -> set[str]:
        return set(re.findall(r"\w+", text.lower()))


cache_service = CacheService()
