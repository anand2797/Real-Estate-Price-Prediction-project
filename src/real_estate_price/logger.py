import os
import logging
from datetime import datetime

log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")

# create directory for logs for store log file
os.makedirs(log_path, exist_ok=True)

#join directory and file to create full path
log_file_path = os.path.join(log_path, log_file)

# create a format to give logging info
format = "[%(asctime)s] %(lineno)d %(name)s- %(levelname)s- %(message)s"

logging.basicConfig(filename=log_file_path,
                    format = format,
                    level=logging.INFO)

