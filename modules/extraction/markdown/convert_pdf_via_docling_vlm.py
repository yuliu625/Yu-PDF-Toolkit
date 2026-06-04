"""
Sources:
    https://github.com/yuliu625/Yu-PDF-Toolkit/blob/main/modules/extraction/markdown/convert_pdf_via_docling_vlm.py

References:
    https://www.docling.ai/

Synopsis:
    通过 docling 提供的 VLM 集成转换 pdf 。

Notes:
    由于各种基于 VLM 的 OCR 工具集成程度较低，这里借用 docling 提供的方法。

    约定:
        - 推理服务: 在大规模使用中，使用本地推理服务或外部 API 服务。
"""

from __future__ import annotations
from loguru import logger

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    ApiVlmOptions,
    ResponseFormat,
    VlmPipelineOptions,
)
from docling.document_converter import (
    DocumentConverter,
    PdfFormatOption,
)
from docling.pipeline.vlm_pipeline import VlmPipeline

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def build_with_vlm_pipeline(
    base_url: str,
    model_name: str,
    vlm_prompt: str,
):
    vlm_options = ApiVlmOptions(
        url=base_url,
        params=dict(
            model=model_name,
        ),
        prompt=vlm_prompt,
        # HARDCODED
        timeout=90,
        scale=1.0,
        response_format=ResponseFormat.MARKDOWN,
    )
    pipeline_options = VlmPipelineOptions(
        enable_remote_services=True,
    )
    # 进行具体配置。
    ## 执行 OCR 。
    # pipeline_options.do_ocr = True
    ## 全页执行
    # pipeline_options.ocr_options.force_full_page_ocr = True
    pipeline_options.vlm_options = vlm_options
    return pipeline_options


def convert_pdf_via_docling_vlm():
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
                pipeline_cls=VlmPipeline,
            )
        }
    )

