import logging

logger = logging

logging.basicConfig(level=logging.INFO,
                    format= '%(asctime)s.%(levelname)s.%(module)s.%(module)s.%(funcName)s.%(message)s',
                    handlers=[logging.FileHandler("hello_flask.log", mode='w'),
                    logging.StreamHandler()])
stream_handler = [h for h in logging.root.handlers if isinstance(
                  h, logging.StreamHandler)][0]
stream_handler.setLevel(logging.INFO)