import sys
import re

def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python3 script.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    unique_urls = set()

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if re.match(r"^https://", line):
                    match = re.match(r"(https://[^/]+)", line)
                    if match:
                        unique_urls.add(match.group(1))

        with open('base_urls.txt', 'w') as output_file:
            for url in unique_urls:
                output_file.write(url + '\n')

    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan!")
        sys.exit(1)

if __name__ == "__main__":
    main()
