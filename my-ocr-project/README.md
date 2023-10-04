# OCR Project

This project allows users to upload an image or PDF file and extract data from it to put into a table. The user can define the output format and select the file for extraction.

## Project Structure

The project has the following files:

- `images/example.png`: This file is an example image that can be uploaded to the application for data extraction.
- `output/example_output.csv`: This file is an example output file that will contain the extracted data in a CSV format.
- `src/main.py`: This file is the entry point of the application. It creates an instance of the Flask app and sets up the routes.
- `src/ocr.py`: This file exports a function `extract_data` which takes an image or PDF file as input and extracts the data from it. The function returns the extracted data in a format specified by the user. The function uses the `pytesseract` library for OCR and the `pdfminer` library for PDF extraction.
- `requirements.txt`: This file lists the dependencies required by the application.
- `README.md`: This file contains the documentation for the project.

## Usage

To use the application, follow these steps:

1. Install the dependencies listed in `requirements.txt`.
2. Run `src/main.py` to start the Flask app.
3. Navigate to `http://localhost:5000` in your web browser.
4. Upload an image or PDF file and specify the output format.
5. Click the "Extract Data" button to extract the data from the file.
6. The extracted data will be displayed in a table on the web page and saved to a CSV file in the `output` directory.

## Dependencies

The application requires the following dependencies:

- Flask
- pytesseract
- pdfminer

These dependencies can be installed by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.