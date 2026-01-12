"""
通过PyMuPDFLLM转换pdf为markdown。
"""

from __future__ import annotations
from loguru import logger

import pymupdf4llm
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def convert_pdf_via_pymupdfllm(
    pdf_path: str | Path,
    result_markdown_path: str | Path,
    is_need_image: bool,
    result_image_dir: str | Path,
) -> None:
    ...

