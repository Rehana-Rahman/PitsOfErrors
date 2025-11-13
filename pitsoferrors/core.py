import random
from pitsoferrors.data import subjects, verbs, adjectives

def build_unique_insults():
    combos = []
    for s in subjects:
        for v in verbs:
            for a in adjectives:
                combos.append(f"{s} {v} {a}.")
    random.shuffle(combos)
    return combos
