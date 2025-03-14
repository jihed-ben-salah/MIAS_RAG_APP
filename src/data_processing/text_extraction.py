from pdf2image import convert_from_path
import pytesseract
import os

# Convert PDF to images
def extract_text_from_pdf(pdf_path):
    """
    use OSC to extract text from a PDF file
    :param pdf_path: path to the PDF file
    """
    images = convert_from_path(pdf_path)
    extracted_text = ""
    for image in images:
        extracted_text += pytesseract.image_to_string(image)
    return extracted_text


def process_dataset(dataset_path, output_path):
    """
    process a dataset of PDF files
    :param dataset_path: path to the dataset
    :param output_path: path to the output file
    """
    documents = os.listdir(dataset_path)
    for doc in documents:
        doc_path = os.path.join(dataset_path, doc)
        text = extract_text_from_pdf(doc_path)
        with open(output_path, "a") as f:
            f.write(text)
            f.write("\n")
    