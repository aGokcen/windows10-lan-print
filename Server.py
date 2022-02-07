__author__ = "Alpaslan GÖKCEN"
__copyright__ = "Copyright 2022"

__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "alpaslan.gokcen@istanbulticaret.edu.tr"
__status__ = "Test"

"""
PROBLEM DEFINITION:
'Inaccessible Shared Printer' after the KB5005565 Update

PDFtoPrinter.exe is taken from
http://www.columbia.edu/~em36/pdftoprinter.html.tor.

To print a PDF file to the default Windows printer, use this command:
PDFtoPrinter.exe filename.pdf "Name of Printer"
"""

import configparser
import os
import time
from glob import glob
from subprocess import Popen, PIPE



def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    file_path = config['DEFAULT']['file_path']
    printer_name = config['DEFAULT']['printer_name']

    # Get Current Directory
    cur_dir = os.getcwd()

    # Change File Directory
    os.chdir(file_path)

    listening = True

    print("System is started...")
    print("Listening...")
    while listening:
        file_list = []

        # GET ALL FILES
        for file in glob("*.pdf"):
            for i in range(10, 1, -1):
                print("\rFile found: "+file+", will be written in " +str(i)+" seconds...", end='')
                time.sleep(1)

            # PRINT ALL FILES
            try:
                process = Popen([os.path.join(cur_dir, 'PDFtoPrinter.exe'), file, printer_name], stdout=PIPE, stderr=PIPE)
                print(f"\rThe file which is named {file} has been sent to the printer {printer_name} ...", end='')
                process.communicate()
                file_list.append(file)
                print(f"\rFile is printed...", end='')
                time.sleep(3)
                print("\r", end='')

            except Exception as e:
                print("Error, something is happened...")
                print(e, file)
                os.remove(file)

        # Sleep 5 Sec
        time.sleep(5)

        # Remove Printed Files
        for file in file_list:
            os.remove(file)
        time.sleep(5)


if __name__ == '__main__':
    main()
