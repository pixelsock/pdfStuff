import pytesseract
from pdfminer.high_level import extract_text


def extract_data(file_path, output_format):
    """
    Extracts data from an image or PDF file and returns it in the specified format.

    Args:
        file_path (str): The path to the file to extract data from.
        output_format (str): The format to return the extracted data in. Can be 'csv' or 'json'.

    Returns:
        str: The extracted data in the specified format.
    """
    # Check if file is PDF or image
    if file_path.endswith('.pdf'):
        text = extract_text(file_path)
    else:
        text = pytesseract.image_to_string(file_path)

    # Process extracted text
    lines = text.split('\n')
    data = []
    for line in lines:
        if line.strip() != '':
            data.append(line.split())

    # Convert data to specified output format
    if output_format == 'csv':
        output = ''
        for row in data:
            output += ','.join(row) + '\n'
    elif output_format == 'json':
        output = []
        headers = data[0]
        for row in data[1:]:
            output.append(dict(zip(headers, row)))
    else:
        raise ValueError('Invalid output format specified.')

    return output