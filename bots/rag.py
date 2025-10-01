from __future__ import annotations
from typing import Optional
import os
import httpx

from .llm import LLMBot


class RAGBot(LLMBot):
    def __init__(self, runtype="custom", stream=True, verbose=False) -> None:
        super().__init__(runtype, stream, verbose)
        self.search_api_baseurl = "https://s.jina.ai/"
        self.search_api_key = os.getenv("JINA_API_KEY")
        self.search_timeout = 30.0
        self.search_result_limit = 32768

    def _retrieve(self, q: str) -> Optional[str]:
        if not self.search_api_key:
            self._print("search api key missing, falling back to plain query", "yellow",)
            return None

        headers = {
            "Authorization": f"Bearer {self.search_api_key}",
            "X-Respond-With": "no-content"
            }
        params = {"q": q}

        try:
            response = httpx.get(
                self.search_api_baseurl,
                params=params,
                headers=headers,
                timeout=self.search_timeout,
            )
            response.raise_for_status()
        except httpx.HTTPError as e:
            self._print(f"retrieving failed: {e}", "red")
            return None

        s = response.text.strip()
        if not s: return None
        if len(s) > self.search_result_limit:
            s = s[:self.search_result_limit].rstrip() + "..."
        return s

    def _preprocessing(self, q: str) -> str:
        q = super()._preprocessing(q)

        context = self._retrieve(q)
        if not context: return q
        prompt = (
            "You are answering a question using additional context fetched from a web search."
            "\n\nContext:\n"
            f"{context}\n\n"
            f"User question: {q}"
        )

        return prompt
