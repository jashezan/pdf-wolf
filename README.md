# pdf-wolf

**pdf-wolf** is a Python-based command-line tool that extracts and merges PDF files or converts PDF pages to PNG images. It provides flexibility to handle page ranges, output formats, and batch operations for merging files.

---

## Features

- **Extract PDF pages**: Extract individual pages from a PDF file as PNG images or separate PDF files.
- **Merge files**: Merge multiple PNG or PDF files in a folder into a single PDF file.
- **Customizable page range**: Specify the range of pages to extract from the PDF file.
- **Platform-independent**: Works on Linux, macOS, and Windows.
- **Error handling**: Provides detailed error messages for incorrect input and invalid operations.

---

## Installation

### Virtual Environment Setup

1. Clone the repository or download the tool.
2. Navigate to the project folder.
3. Set up a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  
# On Windows, use: venv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Create Executable Binary

To create an executable binary for the tool:

1. Install `pyinstaller`:

```bash
pip install pyinstaller
```

2. Generate the binary executable:

```bash
pyinstaller --onefile main.py -n pdfwolf
```

The executable will be available in the `dist/` folder.

---

## Usage

The tool can be used in several different ways. Here are all possible use cases:

### 1. Extracting Pages from a PDF

By default, `pdf-wolf` extracts the first 10 pages of the specified PDF file and saves them as PNG images in a folder named after the input PDF file.

```bash
./pdfwolf demo.pdf
```

Result: Extracts pages 1 to 10 of `demo.pdf` as PNG files into the `demo/` folder.

---

### 2. Extracting Pages in PDF Format

To extract pages as individual PDF files instead of PNG images:

```bash
./pdfwolf demo.pdf -f pdf
```

Result: Extracts pages 1 to 10 of `demo.pdf` as separate PDF files into the `demo/` folder.

---

### 3. Extracting a Custom Range of Pages

To specify a custom range of pages to extract (e.g., pages 5 to 20):

```bash
./pdfwolf demo.pdf -r 5 20
```

Result: Extracts pages 5 to 20 of `demo.pdf` as PNG files into the `demo/` folder.

You can also extract this range in PDF format:

```bash
./pdfwolf demo.pdf -r 5 20 -f pdf
```

Result: Extracts pages 5 to 20 of `demo.pdf` as individual PDF files.

---

### 4. Merging Files into a Single PDF

If you have multiple PNG or PDF files in a folder and want to merge them into a single PDF, use the `--merge` option.

**Example 1**: Merging all PNG files in the `png_files/` folder into a single PDF:

```bash
./pdfwolf --merge --folder png_files -f png
```

Result: Combines all PNG images in `png_files/` into a single PDF called `png_files_merged.pdf`.

**Example 2**: Merging all PDF files in a folder into a single PDF:

```bash
./pdfwolf --merge --folder demo
```

Result: Merges all PDF files in the demo/ folder into demo_merged.pdf.

---

### 5. Help and Usage Information

To view the help message, use:

```bash
./pdfwolf --help
```

Result: Displays the usage information for the tool, including all available options.

```bash
usage: pdfwolf [-h] [-f {png,pdf}] [-r START END] [-m] [--folder FOLDER] [pdf_path]

PDF to Image or PDF extraction and merging tool.

positional arguments:
  pdf_path              Path to the PDF file to extract pages from.

options:
  -h, --help            Show this message and exit.
  -f {png,pdf}, --format {png,pdf}
                        Output format (default: png).
  -r START END, --range START END
                        Page range to extract (default: first 10 pages).
  -m, --merge           Merge all files in folder into a single PDF.
  --folder FOLDER       Folder containing files to merge.
```


## Folder Structure

Below is the example folder structure after running the tool:

```bash
❯ ls -lah
drwxrwxr-x    - shezan 18 Oct 00:57  build/
drwxrwxr-x    - shezan 18 Oct 00:58  dist/
drwxrwxr-x    - shezan 17 Oct 23:30  venv/
.rw-rw-r-- 1.0M shezan 18 Oct 00:50  demo.pdf
.rwxrwxr-x 3.6k shezan 18 Oct 00:37  main.py*
.rw-rw-r--  659 shezan 18 Oct 00:57  pdfwolf.spec
.rw-rw-r--  153 shezan 18 Oct 00:42  requirements.txt
```

After extracting the pages from `demo.pdf`, a new folder `demo/` will be created, containing the output files.


## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.