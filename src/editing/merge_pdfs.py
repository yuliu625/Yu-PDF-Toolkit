"""
Sources:
    https://github.com/yuliu625/Yu-PDF-Toolkit/blob/main/src/editing/merge_pdfs.py

References:
    https://pymupdf.readthedocs.io/en/latest/the-basics.html

Synopsis:
    合并 PDF 文件的方法。

Notes:
    因为原始代码是基于 C 构建的，在 python 文档的代码很简陋，这里只做简单的封装。
"""

from __future__ import annotations
from loguru import logger

import pymupdf
from pathlib import Path

from typing import TYPE_CHECKING, Sequence
# if TYPE_CHECKING:


def merge_2_file(
    input_file_1: str | Path,
    input_file_2: str | Path,
    output_path: str | Path,
) -> None:
    """
    官方文档上合并 2 个文件的方法。

    允许不是 PDF ，需要是支持的文件格式。

    Args:
        input_file_1 (Union[str, Path]): 前面的文件的路径。
        input_file_2 (Union[str, Path]): 后面的文件的路径。
        output_path (Union[str, Path]): 结果路径。

    Returns:
        None: 合并并完成保存。
    """
    logger.trace(f"Input file 1: {input_file_1}")
    logger.trace(f"Input file 2: {input_file_2}")
    # open files
    document_1 = pymupdf.open(input_file_1)
    document_2 = pymupdf.open(input_file_2)
    # merge documents
    document_1.insert_file(document_2)
    # save result
    document_1.save(output_path)
    logger.success(f"Merged. Save to {output_path}")


def merge_pdfs(
    input_pdf_paths: Sequence[str | Path],
    output_path: str | Path,
) -> None:
    """
    按照顺序合并多个 PDF 文件。

    Args:
        input_pdf_paths (Sequence[Union[str, Path]]): 输入的 PDF 的路径，需要按照顺序输入。
        output_path (Union[str, Path]): 结果路径。

    Returns:
        None: 合并并完成保存。
    """
    logger.trace(f"Input pdf paths: {input_pdf_paths}")
    # create an empty document object
    document_master = pymupdf.open()
    # add PDF pages
    for file_path in input_pdf_paths:
        # open target PDF file
        document_item = pymupdf.open(file_path)
        # add document item
        document_master.insert_pdf(document_item)
        # close PDF
        document_item.close()
    # save result
    document_master.save(output_path)
    logger.success(f"Merged. Save to {output_path}")
    # close PDF
    document_master.close()

