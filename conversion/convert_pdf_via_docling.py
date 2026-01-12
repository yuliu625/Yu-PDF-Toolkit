"""
通过docling转换pdf为markdown。
"""

from __future__ import annotations
from loguru import logger

from docling.document_converter import DocumentConverter
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def convert_pdf_via_docling(
    pdf_path: str | Path,
) -> None:
    ...

