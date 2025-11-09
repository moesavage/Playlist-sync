import logging
import os

def get_logger(name: str):
    """
    Returns a configured logger with both console and file output.
    Example: logger = get_logger("playlist_sync")
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers if re-imported
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Create logs directory if needed
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{name}.log")

    # Format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
























# # utils/logger.py
# import logging




# def get_logger(name=__name__):
#     logger = logging.getLogger(name)
#     if not logger.handlers:
#         handler = logging.StreamHandler()
#         fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
#         handler.setFormatter(fmt)
#         logger.addHandler(handler)
#         logger.setLevel(logging.INFO)
#     return logger