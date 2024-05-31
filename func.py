import os
import shutil
import zipfile
from PIL import Image
import img2pdf, pdf2image
import subprocess
import tempfile, pathlib

def main():
    """
    This is the main function of the program.
    It displays a menu and performs actions based on the user's choice.
    """
    print("Menu")
    print("1. Add the cbz file")
    print("2. Add the cbz file and the output directory")
    print("3. reduce pdf size")
    print("4. cbz to pdf and reduce its size")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cbz_file = str(input("Enter the cbz file: ")) # Enter the path of the CBZ file
        convert_cbz_to_pdf(cbz_file)
        main()

    elif choice == 2:
        cbz_file = str(input("Enter the cbz file: "))
        output_dir = str(input("Enter the output directory: "))
        convert_cbz_to_pdf(cbz_file, output_dir )
        main()

    elif choice == 3:
        pdf_file = str(input("Enter the pdf file: "))
        reduce_pdf_size(pdf_file)
        main()

    elif choice == 4:
        cbz_file = str(input("Enter the cbz file: "))
        file = convert_cbz_to_pdf(cbz_file)
        reduce_pdf_size(file)
        main()

    elif choice == 5:
        print("Exiting...")

    else:
        print("Invalid choice. Please try again.")
        main()




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

def img_to_pdf(img_folder, output_pdf=None):
    """
    Converts images in a folder to a PDF file.

    Args:
        img_folder (str): The path to the folder containing the images.
        output_pdf (str, optional): The path to the output PDF file. If not provided, the output file will be named after the image folder.
    """

    # If no output PDF file is provided, create one with the same name as the image folder
    if output_pdf is None:
        output_pdf = f"{img_folder}.pdf"
    else:
        output_pdf = output_pdf+".pdf"

    # Get the list of image files, sorted by filename
    img_files = sorted([f for f in os.listdir(img_folder) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif'))])

    # Create the full paths for the image files
    img_paths = [os.path.join(img_folder, f) for f in img_files]

    # Convert the images to PDF and write them to the output file
    with open(output_pdf, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(img_paths))

def pdf_to_img(pdf_file, output_folder=None, show_mess:bool=None, format:str= None):
    """
        Extract the images from the PDF file and save them to the output folder
        Args:
            pdf_file: The path to the PDF file to extract images from.
            output_folder: The path to the folder where the extracted images will be saved.
    """
    format_list = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp']

        # Extract the images from the PDF file and save them to the output folder
    try:
        if show_mess is None: 
            show_mess = True

        if format is None:
            format = ".jpg"
        else:
            if "."+format not in format_list:
                raise ValueError("Invalid format. Supported formats: jpg, jpeg, png, bmp, gif, webp")
            else:
                format = format.lower()

        if not output_folder:
            output_folder = os.path.splitext(pdf_file)[0]
            os.makedirs(output_folder, exist_ok=True)
            print("Folder Created with name: ",output_folder)

        else:
            print(f"Folder with name {output_folder} if exist, it will proceed to use it")

        print("Extracting the images from the PDF")
        images = pdf2image.convert_from_path(pdf_file)
            
        for i in range(len(images)):
      # Save pages as images in the pdf
            images[i].save(f'{output_folder}/page' + str(i) + format)
            if show_mess:
                print(f"Image {i} saved successfully")

        print("Images extracted successfully")

    except Exception as e:
        print("Error:", e)
        shutil.rmtree(output_folder)
        