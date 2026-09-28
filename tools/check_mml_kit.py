#!/usr/bin/env python3
"""Smoke-check the MML grammar kit XML files and declared local references."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
XML_FILES = [
    ROOT / 'data/grammar/vectors.mml',
    ROOT / 'data/grammar/fold.cd.xml',
    ROOT / 'data/grammar/fold_graph.xml',
]
REFERENCE_PATTERNS = [
    r'(data/grammar/[A-Za-z0-9_.\-]+)',
    r'(data/shaders/[A-Za-z0-9_.\-]+)',
]

def main() -> int:
    errors = []
    refs = set()
    for path in XML_FILES:
        if not path.exists():
            errors.append(f'missing XML: {path.relative_to(ROOT)}')
            continue
        try:
            ET.parse(path)
        except Exception as exc:
            errors.append(f'parse failed: {path.relative_to(ROOT)}: {exc}')
        text = path.read_text(encoding='utf-8', errors='replace')
        for pat in REFERENCE_PATTERNS:
            refs.update(re.findall(pat, text))
    for rel in sorted(refs):
        if not (ROOT / rel).exists():
            errors.append(f'missing reference: {rel}')
    if errors:
        for err in errors:
            print(f'FAIL | {err}')
        return 1
    print(f'PASS | mml-kit: {len(XML_FILES)} XML files parsed, {len(refs)} reference(s) resolved')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
