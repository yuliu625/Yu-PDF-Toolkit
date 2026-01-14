"""
Sources:
    https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/

References:
    https://pypi.org/project/pymupdf4llm/
    https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/api.html#pymupdf4llm-api

Synopsis:
    通过pymupdf4llm转换pdf为markdown。

Notes:
    官方的实现很不优雅，但是方法足够快捷。这些方法可以用于快速获取原型。
"""

from __future__ import annotations
from loguru import logger

import pymupdf4llm
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def convert_pdf_via_pymupdf4llm(
    pdf_path: str | Path,
    result_markdown_path: str | Path,
) -> None:
    # 路径处理。
    result_markdown_path = Path(result_markdown_path)
    result_markdown_path.parent.mkdir(parents=True, exist_ok=True)
    # 执行转换。仅指定路径，其他默认执行。
    markdown_text = pymupdf4llm.to_markdown(
        str(pdf_path),
    )
    logger.trace("Markdown Text: \n", markdown_text)
    # 保存。
    result_markdown_path.write_text(markdown_text, encoding='utf-8')
    logger.success(f"Save markdown to {result_markdown_path}")


def convert_pdf_via_pymupdf4llm_with_images(
    pdf_path: str | Path,
    result_markdown_path: str | Path,
    is_need_image: bool,
    result_image_dir: str | Path,
) -> None:
    # 路径处理。
    result_markdown_path = Path(result_markdown_path)
    result_markdown_path.parent.mkdir(parents=True, exist_ok=True)
    result_image_dir = Path(result_image_dir)
    result_image_dir.mkdir(parents=True, exist_ok=True)
    # 执行转换。要求提取和保存图片。
    markdown_text = pymupdf4llm.to_markdown(
        str(pdf_path),
        write_images=is_need_image,
        image_path=result_image_dir,
    )
    logger.trace("Markdown Text: \n", markdown_text)
    # 保存。
    result_markdown_path.write_text(markdown_text, encoding='utf-8')
    logger.success(f"Save markdown to {result_markdown_path}")

