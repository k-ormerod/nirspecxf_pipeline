from PyPDF2 import PdfMerger
import os
import glob
import shutil


def merge_pdf(directory, output):
 
    # Create a PdfFileMerger object
    merger = PdfMerger()

    # Get a list of PDF files in the directory 
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

    # Sort the PDF files (optional, but often helpful)
    pdf_files.sort() 

    # Add PDFs to the merger 
    for filename in pdf_files:
        filepath = os.path.join(directory, filename)
        merger.append(open(filepath, 'rb'))

    # Write the merged PDF file
    with open(f'{output}.pdf', 'wb') as output_file:
        merger.write(output_file)


def sort(plot_dir):
    files = glob.glob(plot_dir + "*.pdf")
    for plot_type in ["zoom", "full"]:
        if not os.path.exists(plot_dir + plot_type):
            os.makedirs(plot_dir + plot_type)

    for file in files:
        if "zoom" in file:
            try:
                shutil.move(file, plot_dir + "zoom/")
            except:
                print(f"Could not move {file}")
        else :
            try:
                shutil.move(file, plot_dir + "full/")
            except:
                print(f"Could not move {file}")

    for plot_type in ["zoom", "full"]:
        merge_pdf(plot_dir + plot_type + "/", plot_dir + plot_type + "_compilation")

    if not os.path.exists(plot_dir + "comp"):
        os.makedirs(plot_dir + "comp")

    files = glob.glob(plot_dir + "*compilation.pdf")
    
    for file in files:
        try:
            shutil.move(file, plot_dir + "comp/")
        except: 
            print(f"Could not move {file}")

