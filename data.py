"""Read Amazon polarity CSV safely; do not infer labels from row positions."""
import csv
import io
import random
import zipfile
from collections import Counter


def read_amazon_zip(path, sample_size=10000, seed=42):
    """Uniform reservoir sample over a headerless label,title,review CSV."""
    if sample_size < 2:
        raise ValueError('sample_size must be at least 2')
    rng = random.Random(seed)
    sample = []
    counts = Counter()
    with zipfile.ZipFile(path) as archive:
        members = [n for n in archive.namelist() if n.lower().endswith('.csv') and not n.startswith('__MACOSX/')]
        if len(members) != 1:
            raise ValueError(f'Expected exactly one CSV, found {members}')
        with archive.open(members[0]) as raw:
            reader = csv.reader(io.TextIOWrapper(raw, encoding='utf-8-sig', newline=''))
            for index, row in enumerate(reader):
                if len(row) != 3 or row[0] not in {'1', '2'}:
                    raise ValueError(f'Invalid Amazon CSV row {index + 1}; expected label 1/2,title,review')
                label = int(row[0]) - 1
                text = (row[1] + ' ' + row[2]).strip()
                if not text:
                    raise ValueError(f'Empty review at row {index + 1}')
                counts[label] += 1
                item = {'text': text, 'label': label}
                if len(sample) < sample_size:
                    sample.append(item)
                else:
                    slot = rng.randrange(index + 1)
                    if slot < sample_size:
                        sample[slot] = item
    if set(counts) != {0, 1}:
        raise ValueError(f'Both classes required; observed {dict(counts)}')
    return sample, {'source_rows': sum(counts.values()), 'source_labels': dict(counts), 'csv_member': members[0], 'seed': seed}


def clean_text(text):
    import html
    import re
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(text))).strip()
