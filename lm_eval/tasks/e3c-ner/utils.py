import collections
import re
import string

import datasets
import evaluate


def normalize_text(s):
    return s.lower()


def get_tokens(s):
    print([i for i in normalize_text(s).split(", ")])
    return [i for i in normalize_text(s).split(", ")]


def f1(items):
    gold_toks = get_tokens(items[0])
    pred_toks = get_tokens(items[1][10:])
    common = collections.Counter(gold_toks) & collections.Counter(pred_toks)
    num_same = sum(common.values())
    if len(gold_toks) == 0 or len(pred_toks) == 0:
        # If either is no-answer, then F1 is 1 if they agree, 0 otherwise
        return int(gold_toks == pred_toks)
    if num_same == 0:
        return 0
    precision = 1.0 * num_same / len(pred_toks)
    recall = 1.0 * num_same / len(gold_toks)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1
