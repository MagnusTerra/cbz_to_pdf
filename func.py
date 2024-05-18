import os
import shutil
import zipfile
from PIL import Image
import img2pdf
import subprocess
import tempfile


def get_file_directory(file_path):
    # Get the directory of the file
    directory = os.path.dirname(file_path)
    
    # Get the base folder name
    folder_name = os.path.basename(directory)
    
    return folder_name

def cbz_to_pngs(cbz_file, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the CBZ file
    with zipfile.ZipFile(cbz_file, 'r') as cbz:
        # Extract each file in the CBZ archive
        for filename in cbz.namelist():
            # Ensure it's an image file (you can add more extensions if needed)
            if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG','.webp')):
                # Read image data from the CBZ archive
                with cbz.open(filename) as file:
                    # Open the image using PIL
                    img = Image.open(file)
                    # Convert to RGB if the image is not in RGB format
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    # Save the image as a PNG file in the output directory
                    img.save(os.path.join(output_dir, os.path.splitext(os.path.basename(filename))[0] + '.png'))




def create_pdf_from_pngs(png_folder, output_pdf):
    # Get a list of PNG files in the folder
    png_files = [f for f in os.listdir(png_folder) if f.lower().endswith('.png')]

    # Sort the files numerically
    png_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

    # Create a PDF from the PNG files
    with open(output_pdf, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert([os.path.join(png_folder, f) for f in png_files]))

# Convert a CBZ file to a PDF file
def convert_cbz_to_pdf(cbz_file, output_directory=None):
    """
    Converts a CBZ file to a PDF file.

    Args:
        cbz_file (str): The path to the CBZ file.
        output_directory (str, optional): The directory where the output PDF file will be saved. If not provided, a temporary directory will be created.

    Raises:
        FileNotFoundError: If the CBZ file does not exist.
        ValueError: If the CBZ file is not a valid CBZ file.

    Returns:
        None
    """
    
    if output_directory is None:
            
        dir_path = get_file_directory(cbz_file)
        # Create a temporary directory to extract the images
        output_dir = f'{dir_path}/temp_images'
        

        os.makedirs(output_dir, exist_ok=True)

        # Get the base name of the CBZ file (without the extension)
        base_name = os.path.splitext(os.path.basename(cbz_file))[0]
        # Create the name of the output PDF file
        
        output_pdf = os.path.join(dir_path, base_name + '.pdf')

        try:
            print("Extracting the images from the CBZ file")
            # Extract the images from the CBZ file
            cbz_to_pngs(cbz_file, output_dir)
            print("Images extracted successfully")
            print("Creating the PDF from the extracted images")
            # Create the PDF from the extracted images
            create_pdf_from_pngs(output_dir, output_pdf)
        finally:
            # Remove the temporary directory and its contents
            shutil.rmtree(output_dir)
            return output_pdf
    else:  
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)
        temp_dir = f'{output_directory}/temp_images'
        os.makedirs(temp_dir, exist_ok=True)
        # Get the base name of the CBZ file (without the extension)
        base_name = os.path.splitext(os.path.basename(cbz_file))[0]
        # Create the name of the output PDF file
        output_pdf = os.path.join(output_directory, base_name + '.pdf')
        try:
            print("Extracting the images from the CBZ file")
            # Extract the images from the CBZ file
            cbz_to_pngs(cbz_file,temp_dir)
            print("Images extracted successfully")
            print("Creating the PDF from the extracted images")
            # Create the PDF from the extracted images
            create_pdf_from_pngs(temp_dir, output_pdf)
        finally:
            shutil.rmtree(f'{output_directory}/temp_images')
            return output_pdf
        
def reduce_pdf_size(pdf_file):
    """
    Reduces the size of a PDF file using Ghostscript.
    
        Args:
        pdf_file: The path to the PDF file to reduce.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    try:
        print("Reducing the size of the PDF")
        # Call Ghostscript to compress the PDF
        subprocess.call([
            'gs',
            '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            '-dPDFSETTINGS=/screen',  # Change this to /ebook, /printer, or /prepress for different quality
            '-dNOPAUSE',
            '-dBATCH',
            f'-sOutputFile={temp_file.name}',
            pdf_file
        ])
        print("PDF reduced successfully")
        # Copy the temporary file to the original file location
        shutil.copyfile(temp_file.name, pdf_file)
    finally:
        # Clean up the temporary file if it still exists
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
