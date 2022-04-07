import os
import logging

if __name__ == "__main__":
    from .main import run
    logging.getLogger().setLevel(level=logging.INFO)
    run()
