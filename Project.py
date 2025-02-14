
import re
import pytesseract
from PIL import Image
import streamlit as st

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path

with st.sidebar:
    st.image("pblife.GIF")
    st.divider()
    st.write('''Your health is your most important asset.
Protect it with health insurance.
Don’t wait until it’s too late.
Get covered with health insurance now.

Let’s look at how a health
cover can benefit you.

1. Hospitalization Expenses            
2. Health Check Ups
3. No Claim Bonus
4. Income Tax Rebate
5. No Age Barrier''')


def extract_aadhar_number(text):
    aadhar_pattern = r"\b\d{4}\s?\d{4}\s?\d{4}\b"
    matches = re.search(aadhar_pattern, text)
    return matches.group()

def extract_pan_number(text):
    pan_pattern = r"\b[A-Z]{5}\d{4}[A-Z]\b"
    matches = re.search(pan_pattern, text)
    return matches.group()
def extract_dob(text):
    dob_pattern = r"\d{1,2}/\d{1,2}/\d{4}"
    matches = re.search(dob_pattern, text)
    return matches.group()

st.title('''Hello! Welcome to our Health Insurance Portal.''')

uploaded_file = st.file_uploader("Upload Document Image", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image",width = 300)

    image = Image.open(uploaded_file)
    image_text = pytesseract.image_to_string(image)
    
    if "TAX" in image_text:
        pan_numbers = extract_pan_number(image_text)
        dob = extract_dob(image_text)
        st.subheader("Extracted Pan Number")

        if not pan_numbers:
            st.warning("No Pan numbers found.")
        else:
            st.write(pan_numbers)

        st.subheader("D.O.B:")
        if not dob:
            st.warning("No D.O.B found.")
        else:
            st.write(dob)
  
    else:
        aadhar_numbers = extract_aadhar_number(image_text)
        dob = extract_dob(image_text)
        st.subheader("Extracted Aadhar Number")
        if not aadhar_numbers:
            st.warning("No Aadhar numbers found.")
        else:
            st.write(aadhar_numbers)
        st.subheader("D.O.B:")
        if not dob:
            st.warning("No D.O.B found.")
        else:
            st.write(dob)

    
