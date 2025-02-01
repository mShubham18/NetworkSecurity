import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error: {self.error_message} at line {self.lineno} in file {self.filename}"

if __name__ == "__main__":
    try:
        logger.logging.info("This is a test log")
        a=1/0
        print(a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)