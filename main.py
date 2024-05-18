from func import *


#Notes1: put a opcion to conver all the cbz files in a folder
#Notes2: future feature: reduce pdf size with ghostscript or other library
#issue: remove the simple and double quotes from the input, cbz_file dont exist 

def main():
    """
    This is the main function of the program.
    It displays a menu and performs actions based on the user's choice.
    """
    print("Menu")
    print("1. Add the cbz file")
    print("2. Add the cbz file and the output directory")
    print("3. reduce pdf size")
    print("4.exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cbz_file = str(input("Enter the cbz file: ")) # Enter the path of the CBZ file
        convert_cbz_to_pdf(cbz_file)
    elif choice == 2:
        cbz_file = str(input("Enter the cbz file: "))
        output_dir = str(input("Enter the output directory: "))
        convert_cbz_to_pdf(cbz_file, output_dir )

    elif choice == 3:
        pdf_file = str(input("Enter the pdf file: "))
        reduce_pdf_size(pdf_file)
    elif choice == 4:
        print("Exiting...")

if __name__ == "__main__":
    main()
