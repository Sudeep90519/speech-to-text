import logging
import os
from datetime import datetime

logging.basicConfig(
    filename="LogFile.log",
    format= "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    )