import logging
import os
from typing import Any

from crewai.tools.base_tool import BaseTool
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class LLMAnalyzerCustomToolInput(BaseModel):
    content_to_summarize: str = Field(
        title="Content to be summarized",
        description="String containing the content to be summarized.",
    )


class LLMAnalyzerCustomTool(BaseTool):
    name: str = "Summarize content and key insights."
    description: str = ("A tool that be used to summarize the content given and list key insights.")
    llm_backend: Any

    def _run(self, content_to_summarize: str) -> str:
        input = content_to_summarize
        system_prompt = "You are tasked with analyzing and summarizing the content provided, particularly from the IT operations domain. Please summarize and make note of any key insights."
        try:
            response = self.llm_backend.inference(system_prompt, input)
            logger.info(f"LLMAnalyzerCustomTool NL prompt received: {content_to_summarize}")
            logger.info(f"LLMAnalyzerCustomTool function arguments identified are: {response}")
            print(f"LLMAnalyzerCustomTool NL prompt received: {content_to_summarize}")
            print(f"LLMAnalyzerCustomTool function arguments identified are: {response}")
            return response
        except Exception as e:
            print(f"LLMAnalyzerCustomTool error summarizing: {str(e)}")
            logger.error(f"LLMAnalyzerCustomTool error summarizing: {str(e)}")
            return None
