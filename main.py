from Tester import Tester
from datetime import datetime


def main():
    tester = Tester(
        url="https://www.google.com",
        timeout=1,
        log_file_path=f"./logs/log_file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
    while True:
        tester \
            .run() \
            .save_elapsed() \
            .print_elapsed()


if __name__ == "__main__":
    main()
