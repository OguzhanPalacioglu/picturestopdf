import os
import io
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait

# Specify the folder where the images are located
image_folder = 'Your pictures path'

# PDF output name
output_pdf = 'output_pdf.pdf'

#create pdf object
pdf_writer = PdfWriter()

# Get and sort all the images in the folder
images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")], key=lambda x: int(x.split("_")[1].split(".")[0]))


# Add each image to PDF file
for image in images:
    image_path = os.path.join(image_folder, image)
    with open(image_path, 'rb') as f:
        img = Image.open(f)
        # create new pdf file
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=img.size)
        can.drawImage(image_path, 0, 0)
        can.showPage()
        can.save()
        packet.seek(0)
        pdf_page = PdfReader(packet).pages[0]
        # Add page on PDF file
        pdf_writer.add_page(pdf_page)

# Save PDF File
with open(output_pdf, 'wb') as f:
    pdf_writer.write(f)
