#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function to process the log input"""
    line_count = 0
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    valid_status_codes = status_codes.keys()

    pattern = r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

    try:
        for line in sys.stdin:
            line_count += 1

            match = re.match(pattern, line.strip())
            if match:
                status_code, file_size = match.groups()

                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

                try:
                    status_code_int = int(status_code)
                    if status_code_int in valid_status_codes:
                        status_codes[status_code_int] += 1
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
