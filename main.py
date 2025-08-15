
import re
import pandas as pd
from pdfminer.high_level import extract_text
import os

def extract_pdf_data(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found.")
        return None
    
    try:
        text = extract_text(pdf_path)
        if not text.strip():
            print("Warning: PDF has no readable text.")
            return None
        
        emails = re.findall(r'\S+@\S+', text)
        amounts = re.findall(r'\b\d+\.\d{2}\b', text)

        if not emails and not amounts:
            print("No matching data found in PDF.")
            return None 
        
        return {"Email": emails,"Amount": amounts}

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    
def save_to_csv(data,output_file="extracted_data.csv"):
    try:
        max_len = min(len(data["Email"]), len(data["Amount"]))
        emails = data["Email"][:max_len]
        amounts = data["Amount"][:max_len]
        
        df = pd.DataFrame({
            "Email": emails,
            "Amount": amounts
        })
        df.to_csv(output_file,index=False)
        print(f"Data saved to '{output_file}'")
    except Exception as e:
        print(f"Error saving CSV: {e}")

if __name__ == "__main__":
    pdf_path = "sample.pdf"

    print("Extracting data from PDF..")
    data = extract_pdf_data(pdf_path)

    if data:
        save_to_csv(data)