"""
通过PyMuPDF转换pdf为markdown。
"""

from __future__ import annotations
from loguru import logger

import fitz
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def convert_pdf_via_pymupdf(
    pdf_path: str | Path,
    result_path: str | Path,
) -> None:
    ...

