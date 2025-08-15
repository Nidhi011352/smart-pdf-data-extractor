
Overview:
This Python script extracts **email addresses** and **amount values** from a PDF file and saves the results into a CSV file.  
It uses **pdfminer** for PDF text extraction, **regex** for pattern matching, and **pandas** for CSV handling.



Features
- Extracts all valid email addresses from PDFs  
- Extracts amounts in formats like `₹200`, `Rs. 1,200`, or `199.99`  
- Saves data in a clean `Email,Amount` CSV format  
- Avoids blank rows by only keeping valid Email + Amount pairs  



Project Structure
.
├── main.py # Main script
├── sample.pdf # Example PDF file
├── extracted_data.csv # Output file (generated after running script)
└── README.md # Documentation


Installation

1. Clone this repository or download the files.
2. Install dependencies:
   pip install pdfminer.six pandas

▶Usage
Place your target PDF file in the project folder (e.g., sample.pdf).

Run the script:
   python main.py

The extracted results will be saved in extracted_data.csv.

📝 Example Output

Email,Amount
test@example.com,₹200
info@abc.com,Rs. 500


📊 How it Works
PDF File → Extract Text → Find Emails & Amounts → Save to CSV

flowchart LR
    A[PDF File] --> B[Extract Text with pdfminer]
    B --> C[Find Emails using Regex]
    B --> D[Find Amounts using Regex]
    C & D --> E[Save to CSV with Pandas]


📌 Notes
Regex patterns are inside main.py and can be updated for different formats.

The script uses min() to ensure only valid Email + Amount pairs are stored (avoids blank rows).

Works with most PDFs, but scanned image PDFs may require OCR tools like Tesseract.


