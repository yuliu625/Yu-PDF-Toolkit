"""
测试docling相关的工具。
"""

from __future__ import annotations
import pytest
from loguru import logger

from conversion.convert_pdf_via_docling import (
    build_pdf_pipeline_options,
    convert_pdf_via_docling,
    batch_convert_pdf_via_docling,
)

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestConvertPdfViaDocling:
    @pytest.mark.parametrize(
        'pdf_path, result_markdown_path', [
        (r"D:\dataset\smart\experimental_datasets\sample_1\000004.pdf",
         r"D:\dataset\smart\tests\docling_1\000004.md"),
    ])
    def test_convert_pdf_via_docling(
        self,
        pdf_path: str,
        result_markdown_path: str,
    ):
        pipeline_options = build_pdf_pipeline_options(
            is_do_table_structure=True,
            is_do_ocr=False,
            images_scale=2.0,
            is_extract_images=False,
        )
        convert_pdf_via_docling(
            pdf_path=pdf_path,
            result_markdown_path=result_markdown_path,
            pipeline_options=pipeline_options,
        )

    @pytest.mark.parametrize(
        'pdf_path, result_markdown_path', [
        (r"D:\dataset\smart\experimental_datasets\sample_1\000004.pdf",
         r"D:\dataset\smart\tests\docling_2\000004.md"),
    ])
    def test_convert_pdf_via_docling_with_images(
        self,
        pdf_path: str,
        result_markdown_path: str,
    ):
        pipeline_options = build_pdf_pipeline_options(
            is_do_table_structure=True,
            is_do_ocr=False,
            images_scale=2.0,
            is_extract_images=True,
        )
        convert_pdf_via_docling(
            pdf_path=pdf_path,
            result_markdown_path=result_markdown_path,
            pipeline_options=pipeline_options,
        )

