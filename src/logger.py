import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory where logs will be saved
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',  # Append mode, creates file if it doesn't exist
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# # Test logging functionality
# if __name__ == "__main__":
#     logging.info("Logging has started")
#     logging.warning("This is a warning")
#     logging.error("This is an error")
