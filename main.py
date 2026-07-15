from loguru import logger
import sys
from backend.api.db import get_db_url, init_db

def main():    
    # 1. Clear default console logger to avoid duplicate screen prints
    logger.remove() 
    logger.add(sys.stderr, level="INFO")
    # 2. Add your file logger EXACTLY ONCE here
    logger.add("project.log", format="{time} | {level} | {message}")

    logger.info("Main application started!")
    get_db_url()
    init_db()

if __name__ == "__main__":
    main()
