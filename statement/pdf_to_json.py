from tabula import *
import datetime


def convert_to_json(file_path):
    read_data = read_pdf(file_path, output_format="json", pages="all")
    return read_data
    
