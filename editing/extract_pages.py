"""
Sources:
    https://github.com/yuliu625/Yu-PDF-Toolkit/editing/extract_pages.py

References:
    https://pymupdf.readthedocs.io/en/latest/the-basics.html

Synopsis:
    提取 PDF 指定的页面。

Notes:
    因为原始代码是基于 C 构建的，在 python 文档的代码很简陋，这里只做简单的封装。
"""

from __future__ import annotations
from loguru import logger

import pymupdf
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def extract_pages(
    input_pdf_path: str | Path,
    output_pdf_path: str | Path,
    page_numbers: list | range,
) -> None:
    """
    提取指定的连续页面。

    Args:
        input_pdf_path (Union[str, Path]): 输入的 PDF 的路径。
        output_pdf_path (Union[str, Path]): 结果路径。
        page_numbers (Union[list, range]): 页面的范围。

    Returns:
        None: 提取并完成操作。
    """
    # open PDF file
    document = pymupdf.open(input_pdf_path)
    # select pages
    logger.info(f"Page numbers: {page_numbers}")
    document.select(page_numbers)
    # save result
    document.save(output_pdf_path)
    logger.success(f"Extracted pages from {input_pdf_path} to {output_pdf_path}")
    document.close()

