import sys
from pathlib import Path
from stats import get_num_words

def main():
    if len(sys.argv) < 2:
        # keep output minimal; Boot.dev usually tests CLI by passing a path
        print("Usage: python main.py <path-to-text>")
        raise SystemExit(1)

    path = sys.argv[1]
    text = Path(path).read_text(encoding="utf-8")
    # print only the number so tests can match exactly
    print(get_num_words(text))

if __name__ == "__main__":
    main()
