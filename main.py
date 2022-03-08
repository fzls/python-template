import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--example", default="默认参数", type=str, help="示例参数")

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    print(f"main: {args}")


if __name__ == "__main__":
    main()
