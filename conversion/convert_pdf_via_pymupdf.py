"""
Sources:
    https://github.com/yuliu625/Yu-PDF-Toolkit/conversion/convert_pdf_via_pymupdf.py

References:
    https://pymupdf.readthedocs.io/en/latest/about.html
    https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/api.html#pymupdf4llm-api

Synopsis:
    通过PyMuPDF转换pdf为txt。

Notes:
    底层的pdf处理方法。简单使用，不是markdown格式。
"""

from __future__ import annotations
from loguru import logger

import fitz
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def convert_pdf_via_pymupdf(
    pdf_path: str | Path,
    result_txt_path: str | Path,
) -> None:
    # 路径处理。
    result_txt_path = Path(result_txt_path)
    result_txt_path.parent.mkdir(parents=True, exist_ok=True)
    # 打开。
    doc = fitz.open(pdf_path)
    all_text = []
    # 遍历每一页。
    for page in doc:
        page_text = page.get_text()
        all_text.append(page_text)
        logger.trace(f"Page Text:\n", page_text)
    # 保存
    result_txt_path.write_text("\n\n".join(all_text), encoding='utf-8')
    logger.success(f"Save txt to {result_txt_path}")


def convert_pdf_via_pymupdf_with_ocr(
    pdf_path: str | Path,
    result_txt_path: str | Path,
) -> None:
    # 路径处理。
    result_txt_path = Path(result_txt_path)
    result_txt_path.parent.mkdir(parents=True, exist_ok=True)
    # 打开。
    doc = fitz.open(pdf_path)
    all_text = []
    # 遍历每一页。
    for page in doc:
        tp = page.get_textpage_ocr(flags=3)
        page_text = tp.extractText()
        all_text.append(page_text)
        logger.trace(f"Page Text:\n", page_text)
    # 保存
    result_txt_path.write_text("\n\n".join(all_text), encoding='utf-8')
    logger.success(f"Save txt to {result_txt_path}")

