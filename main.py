import argparse

from log import logger, add_file_handler

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--example", default="默认参数", type=str, help="示例参数")

    args = parser.parse_args()

    return args


def main():
    add_file_handler(logger_name="main", log_directory="logs", deal_with_multiprocessing=False)

    args = parse_args()

    logger.info(f"main: {args}")


if __name__ == "__main__":
    main()
