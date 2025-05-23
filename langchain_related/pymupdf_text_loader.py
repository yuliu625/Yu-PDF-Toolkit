"""
由langchain中支持的loader实现加载文档。

基础的，基于PyMuPDF4LLMLoader的实现。
"""

from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_community.document_loaders.parsers import RapidOCRBlobParser
from langchain_community.document_loaders.parsers import LLMImageBlobParser
from langchain_openai import ChatOpenAI
from langchain_core.rate_limiters import InMemoryRateLimiter

from pathlib import Path
import os

from langchain_core.language_models import BaseChatModel
from langchain_core.documents import Document
from typing import Literal


class PymupdfTextLoader:
    """
    pymupdf不同加载pdf的方法。
    3种方法对应不同精细程度的加载方法。
    """
    def __init__(
        self,
        pdf_path: str | Path,
    ):
        self.pdf_path = Path(pdf_path)
        self.loader = None

    def run(
        self,
        loading_method: Literal['rule', 'ocr', 'vlm'] = 'rule',
    ) -> list[Document]:
        """
        主要方法。

        Args:
            loading_method: 加载pdf的方法，指定为['rule', 'ocr', 'vlm', ]中的一个。

        Returns:
            langchain中的Document对象。
            我的默认设置使得加载结果是markdown格式的一个文本对象，会在之后被node-parser处理。
        """
        if loading_method == "rule":
            self.set_rule_loader()
            print(f"loading text pdf by {loading_method}")
        elif loading_method == "ocr":
            print(f"loading text pdf by {loading_method}")
            self.set_ocr_loader()
        elif loading_method == "vlm":
            print(f"loading text pdf by {loading_method}")
            self.set_vlm_loader()
        documents: list[Document] = self.loader.load()
        return documents

    def set_rule_loader(self):
        """
        仅提取文档中的文字。
        """
        loader = PyMuPDF4LLMLoader(
            file_path=self.pdf_path,
            mode='single',
            table_strategy='lines',
        )
        self.loader = loader

    def set_ocr_loader(self):
        """
        使用ocr强化文档识别。
        """
        loader = PyMuPDF4LLMLoader(
            file_path=self.pdf_path,
            mode='single',
            extract_images=True,
            images_parser=RapidOCRBlobParser(),
            table_strategy='lines',
        )
        self.loader = loader

    def set_vlm_loader(self):
        """
        使用VLM强化文档识别。
        """
        loader = PyMuPDF4LLMLoader(
            file_path=self.pdf_path,
            mode='single',
            extract_images=True,
            images_parser=LLMImageBlobParser(
                model=self._get_vlm()
            ),
            table_strategy='lines',
        )
        self.loader = loader

    def _get_vlm(self) -> BaseChatModel:
        """
        获取VLM，用于识别pdf文档。
        仅在set_vlm_loader中使用。

        Returns:
            VLM。这里用的是qwen最好的VLM。
        """
        vlm = ChatOpenAI(
            model='qwen-vl-ocr-latest',
            base_url=os.environ['DASHSCOPE_API_BASE_URL'],
            api_key=os.environ['DASHSCOPE_API_KEY'],
            # rate_limiter=InMemoryRateLimiter(
            #
            # ),
        )
        return vlm

