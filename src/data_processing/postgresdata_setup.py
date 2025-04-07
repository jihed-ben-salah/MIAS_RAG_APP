import os
import fitz  # PyMuPDF
import psycopg2
from psycopg2 import sql

# Database connection settings
DB_NAME = "your_database"
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

# Extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    return text.strip() if text else None

# Store extracted text in PostgreSQL
def store_text_in_db(filename, content):
    conn = connect_db()
    cursor = conn.cursor()
    insert_query = sql.SQL("INSERT INTO documents (filename, content) VALUES (%s, %s)")
    cursor.execute(insert_query, (filename, content))
    conn.commit()
    cursor.close()
    conn.close()

# Process all PDFs in a directory
def process_pdfs(pdf_dir):
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        if text:
            store_text_in_db(pdf_file, text)
            print(f"Stored {pdf_file} in DB")
        else:
            print(f"Skipping {pdf_file} (no text found)")

# Run the pipeline
PDF_FOLDER = "pdf_dataset"
process_pdfs(PDF_FOLDER)
