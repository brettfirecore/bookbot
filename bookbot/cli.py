import argparse
from .core import analyze, top_words

def build_parser():
    p = argparse.ArgumentParser(prog="bookbot", description="Analyze text files.")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("analyze", help="print basic stats")
    a.add_argument("path")

    t = sub.add_parser("stats", help="show top N words")
    t.add_argument("path")
    t.add_argument("--top", type=int, default=10)

    return p

def main():
    p = build_parser()
    args = p.parse_args()
    if args.cmd == "analyze":
        print(analyze(args.path))
    elif args.cmd == "stats":
        for word, count in top_words(args.path, args.top):
            print(f"{word}\t{count}")
