import zipfile
import xml.etree.ElementTree as ET
from typing import List

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def get_paragraphs(file_path: str) -> List[str]:
    """Extract all non-empty paragraphs from a docx file."""
    with zipfile.ZipFile(file_path) as z:
        xml = z.read('word/document.xml')
    tree = ET.fromstring(xml)
    paragraphs = []
    for p in tree.iter(WORD_NAMESPACE + 'p'):
        texts = [t.text for t in p.iter(WORD_NAMESPACE + 't') if t.text]
        para_text = ''.join(texts).strip()
        if para_text:
            paragraphs.append(para_text)
    return paragraphs
