import logging
import os

# Takes a string variable as a name and creates a Python logger of the
# same name. Also, creates a 'log' directory and a 'name'.log file (if one
# doesn't already exist) to output the logs to.
def create_logger(name, level=logging.INFO):
    
    # Create the log directory
    log_directory = os.path.join(os.path.dirname(__file__), 'log')
    log_file = os.path.join(log_directory, f'{name}.log')

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Check if logger has handlers
    if not logger.handlers:

        # Create output format handler
        outputStreamHandler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] - %(name)s [%(levelname)s] - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S.%f')
        outputStreamHandler.setFormatter(formatter)
        
        # Create a file handler
        logFileHandler = logging.FileHandler(log_file)
        
        # Add handlers to logger
        logger.addHandler(outputStreamHandler)
        logger.addHandler(logFileHandler)

    return logger

# Create a global logger for this app
logger = create_logger('Olympus')