from pypdf import PdfReader, PdfWriter

def split_pdf_by_ranges(input_pdf_path, output_ranges):
    """
    Splits a PDF into multiple files based on specified page ranges.

    Parameters:
    - input_pdf_path (str): Path to the source PDF file.
    - output_ranges (list of tuples): Each tuple should contain:
        - output path (str)
        - start page (int, 1-based index)
        - end page (int, inclusive, 1-based index)
    """
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)

    for output_path, start, end in output_ranges:
        writer = PdfWriter()

        # Convert to 0-based index and validate
        start_index = max(start - 1, 0)
        end_index = min(end, total_pages)

        if start_index >= end_index:
            print(f"Invalid range for {output_path}: start={start}, end={end}")
            continue

        for i in range(start_index, end_index):
            writer.add_page(reader.pages[i])

        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"Created: {output_path} (Pages {start} to {end})")

# 🔧 Example usage
input_pdf = "Source.pdf"
ranges = [
    ("Section1.pdf", 7, 145),   # Nahw
    #("Section2.pdf", 151, 301),   # Sarf
    ("Section2.pdf", 304, 357),    # Adv Nahw
    ("Section3.pdf", 360, 416)    # Adv Struc
]

split_pdf_by_ranges(input_pdf, ranges)
