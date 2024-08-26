import sys
from src.real_estate_price.logger import logging
import os

def error_message_details(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()

    # file name in which error occured
    filepath = exc_tb.tb_frame.f_code.co_filename
    _, filename = os.path.split(filepath)

    # fuction name in which error occured
    function_name = exc_tb.tb_frame.f_code.co_name

    # line number where error orrured in file
    line_no = exc_tb.tb_lineno 

    error_message = (f'''Error Occured in Script [{filename}], 
                         fuction name: [{function_name}], 
                         line number: [{line_no}],
                         Error: [{str(error)}]''')
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self) -> str:
        return self.error_message