"""
Sources:
    https://github.com/yuliu625/Yu-PDF-Toolkit/conversion/convert_pdf_via_docling.py

References:
    https://www.docling.ai/

Synopsis:
    通过docling转换pdf为markdown。

Notes:
    docling官方文档写的不是很好，该实现后续或许需要修改和更新。

    docling完全按照OOP设计，需要理解设计的模型才能进行。
    docling2.x有破坏性API更新，需要进行修改。

    注意:
        - PipelineOptions是多层极其复杂的配置数据类。
"""

from __future__ import annotations
from loguru import logger

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
    TesseractOcrOptions,
)
from docling.document_converter import (
    DocumentConverter,
    PdfFormatOption,
)
from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from docling.datamodel.pipeline_options import PipelineOptions


def set_pdf_pipeline(
    is_do_table_structure: bool,
    is_calculate_linear_cells: bool,
    is_do_ocr: bool,
    images_scales: float,
    is_extract_images: bool,
) -> PdfPipelineOptions:
    pipeline_options = PdfPipelineOptions()
    # 进行具体配置。
    ## 解析表格
    pipeline_options.do_table_structure = is_do_table_structure
    ## 计算网格。
    pipeline_options.calculate_linear_cells = is_calculate_linear_cells
    ## 执行OCR。
    pipeline_options.ocr = is_do_ocr
    # 如果执行OCR，需要配置具体OCR。
    if is_do_ocr:
        # 这里进行硬编码，后续根据需求更新。
        pipeline_options.ocr_options = TesseractOcrOptions()
    ## 提取图像。
    pipeline_options.images_scales = images_scales
    pipeline_options.generate_picture_images = is_extract_images
    return pipeline_options


def convert_pdf_via_docling(
    pdf_path: str | Path,
    result_markdown_path: str | Path,
    pipeline_options: PdfPipelineOptions,
) -> None:
    # 处理路径。
    result_markdown_path = Path(result_markdown_path)
    result_markdown_path.parent.mkdir(parents=True, exist_ok=True)
    # 构建转换器。
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    # 执行转换。
    result = converter.convert(
        source=pdf_path,
    )
    # 选择需要的导出类型。
    ## HARDCODED: 这里默认导出为markdown。
    markdown_text = result.document.export_to_markdown()
    result_markdown_path.write_text(markdown_text, encoding='utf-8')
    logger.success(f"Save {result_markdown_path}")


def batch_convert_pdf_via_docling(
    pdf_paths: list[str | Path],
    result_markdown_paths: list[str | Path],
    pipeline_options: PdfPipelineOptions,
) -> None:
    """
    批量转换pdf的方法。

    docling需要加载模型，而分别多次加载会消耗大量资源，因此构建该方法。
    注意，该方法包含大量约定，包括:
        - 所有pdf在同一dir下。
        - 所有结果会存储在同一dir下。
    未来根据需要进行重构。

    Args:
        pdf_paths:
        result_markdown_paths:
        pipeline_options:

    Returns:

    """
    # 处理路径。
    ## HACK: 这里近通过第一个路径进行处理。
    result_markdown_path_0 = Path(result_markdown_paths[0])
    result_markdown_path_0.parent.mkdir(parents=True, exist_ok=True)
    # 构建转换器。
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    # 执行转换。
    for _i, pdf_path in enumerate(pdf_paths):
        result = converter.convert(
            source=pdf_path,
        )
        # 选择需要的导出类型。
        ## HARDCODED: 这里默认导出为markdown。
        markdown_text = result.document.export_to_markdown()
        result_markdown_paths[_i].write_text(markdown_text, encoding='utf-8')
        logger.success(f"Save {result_markdown_paths[_i]}")

