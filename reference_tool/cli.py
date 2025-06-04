import argparse
import csv
from .docx_utils import get_paragraphs
from .crossref import search


def main():
    parser = argparse.ArgumentParser(description="Find references for docx paragraphs.")
    parser.add_argument('file', help='input docx file')
    parser.add_argument('-o', '--output', default='references.csv', help='CSV output path')
    parser.add_argument('-n', '--number', type=int, default=3, help='references per paragraph')
    args = parser.parse_args()

    paragraphs = get_paragraphs(args.file)
    print("Paragraphs:")
    for idx, para in enumerate(paragraphs, 1):
        prefix = para[:60]
        suffix = '...' if len(para) > 60 else ''
        print(f"{idx:>3}: {prefix}{suffix}")

    selection = input("Select paragraph numbers (comma separated): ").strip()
    if not selection:
        print("No paragraphs selected.")
        return
    selected = [int(x)-1 for x in selection.split(',') if x.strip().isdigit()]

    with open(args.output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['paragraph', 'title', 'doi'])
        for idx in selected:
            if 0 <= idx < len(paragraphs):
                refs = search(paragraphs[idx], rows=args.number)
                for ref in refs:
                    writer.writerow([idx + 1, ref['title'], ref['doi']])
    print(f"Saved references to {args.output}")


if __name__ == '__main__':
    main()
