import os
import sys
import argparse
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def extract_pages(input_pdf, output_format='png', page_range=(1, 10)):
    # Create output directory based on input pdf file name
    output_dir = Path(input_pdf).stem
    output_dir_path = Path.cwd() / output_dir
    output_dir_path.mkdir(exist_ok=True)

    # Extract pages as images or PDFs
    try:
        if output_format == 'png':
            images = convert_from_path(input_pdf, first_page=page_range[0], last_page=page_range[1])
            for i, img in enumerate(images):
                output_file = output_dir_path / f"page_{i + page_range[0]}.png"
                img.save(output_file)
        elif output_format == 'pdf':
            reader = PdfReader(input_pdf)
            for page_num in range(page_range[0] - 1, min(page_range[1], len(reader.pages))):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])
                output_file = output_dir_path / f"page_{page_num + 1}.pdf"
                with open(output_file, "wb") as f:
                    writer.write(f)
    except Exception as e:
        print(f"Error extracting pages: {e}")
        sys.exit(1)

def merge_files(folder, output_file, output_format='pdf'):
    try:
        files = sorted(Path(folder).glob(f"*.{output_format}"))
        if output_format == 'png':
            images = [Image.open(f) for f in files]
            images[0].save(output_file, save_all=True, append_images=images[1:], resolution=100.0)
        elif output_format == 'pdf':
            merger = PdfMerger()
            for f in files:
                merger.append(str(f))
            with open(output_file, "wb") as f:
                merger.write(f)
    except Exception as e:
        print(f"Error merging files: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="PDF to Image or PDF extraction and merging tool.")
    
    parser.add_argument("pdf_path", nargs='?', help="Path to the PDF file to extract pages from.")
    parser.add_argument("-f", "--format", choices=['png', 'pdf'], default='png', help="Output format (default: png).")
    parser.add_argument("-r", "--range", nargs=2, type=int, metavar=('START', 'END'), default=(1, 10),
                        help="Page range to extract (default: first 10 pages).")
    parser.add_argument("-m", "--merge", action="store_true", help="Merge all files in folder into a single PDF.")
    parser.add_argument("--folder", help="Folder containing files to merge.")
    
    args = parser.parse_args()
    
    if not args.pdf_path and not args.merge:
        parser.print_help()
        sys.exit(1)
    
    if args.pdf_path:
        input_pdf = Path(args.pdf_path)
        if not input_pdf.is_file():
            print(f"Error: File '{args.pdf_path}' does not exist.")
            sys.exit(1)
        
        extract_pages(input_pdf, output_format=args.format, page_range=(args.range[0], args.range[1]))
    
    if args.merge:
        if not args.folder:
            print("Error: Please provide a folder to merge files from.")
            sys.exit(1)
        folder_path = Path(args.folder)
        if not folder_path.is_dir():
            print(f"Error: Folder '{args.folder}' does not exist.")
            sys.exit(1)
        output_file = f"{folder_path.stem}_merged.pdf"
        merge_files(folder_path, output_file, output_format=args.format)

if __name__ == "__main__":
    main()
