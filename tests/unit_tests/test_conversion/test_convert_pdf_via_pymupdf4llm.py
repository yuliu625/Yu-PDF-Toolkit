"""
测试pymupdf4llm相关的工具。
"""

from __future__ import annotations
import pytest
from loguru import logger

from conversion.convert_pdf_via_pymupdf4llm import (
    convert_pdf_via_pymupdf4llm,
    convert_pdf_via_pymupdf4llm_with_images,
)

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestConvertPDFViaPymupdf4llm:
    @pytest.mark.parametrize(
        'pdf_path, result_markdown_path', [
        (r"",
         r""),
    ])
    def test_convert_pdf_via_pymupdf4llm(
        self,
        pdf_path,
        result_markdown_path,
    ):
        convert_pdf_via_pymupdf4llm(
            pdf_path=pdf_path,
            result_markdown_path=result_markdown_path,
        )

    @pytest.mark.parametrize(
        'pdf_path, result_markdown_path, is_need_images, result_image_dir', [
        (r"",
         r"",
         True,
         r"",),
    ])
    def test_convert_pdf_via_pymupdf4llm_with_images(
        self,
        pdf_path,
        result_markdown_path,
        is_need_images,
        result_image_dir,
    ):
        convert_pdf_via_pymupdf4llm_with_images(
            pdf_path=pdf_path,
            result_markdown_path=result_markdown_path,
            is_need_image=is_need_images,
            result_image_dir=result_image_dir,
        )

