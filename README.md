# Reference Tool

This project provides a simple command line interface for extracting paragraphs from a Word
file and searching for related references using the Crossref API. The results are stored in
a CSV file containing the paragraph number, reference title and DOI.

## Usage

```
python -m reference_tool.cli <document.docx> -n 3 -o output.csv
```

The program displays each paragraph and prompts for the paragraphs that require
references.
