import collections
import re
import string

import datasets
import evaluate
from scipy.stats import spearmanr


def spearman_corr(items):
    """
    Compute Spearman correlation between model predictions and gold targets.
    `results` is a list of (gold, prediction) tuples, both as strings.
    """
    convert_items = []
    for i in items:
        try:
            convert_items.append(float(i[:3]))
        except:
            convert_items.append(0.0)
    return convert_items


def spearman_agg(items):
    golds = list(zip(*items))[0]
    preds = list(zip(*items))[1]
    spearmanr_score = spearmanr(golds, preds)
    return {"Value" : round(spearmanr_score.statistic, 3), "pvalue" : spearmanr_score.pvalue}
