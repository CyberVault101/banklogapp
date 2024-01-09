import logging

# Configure the logging
logging.basicConfig(filename='my_log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
logging.info('This is an informational message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
