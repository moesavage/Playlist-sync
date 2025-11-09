# utils/matching.py
from rapidfuzz import fuzz




def normalize_text(s):
    if not s:
        return ''
    return ''.join(ch for ch in s.lower() if ch.isalnum() or ch.isspace()).strip()




def fuzzy_score(a, b):
    return fuzz.token_sort_ratio(normalize_text(a), normalize_text(b))




def choose_best_candidate(source_title, source_artist, candidates):
    best = None
    best_score = 0
    source_combined = f"{source_title} {source_artist}"
    for c in candidates:
        candidate_combined = f"{c.get('title','')} {c.get('artist','') or c.get('artists','') or ''}"
        score = fuzzy_score(source_combined, candidate_combined)
        if score > best_score:
            best_score = score
            best = c
    return best, best_score
























# from rapidfuzz import fuzz

# def match_track(source, candidates):
#     best = None
#     best_score = 0
#     for c in candidates:
#         score = fuzz.token_sort_ratio(f"{source['title']} {source['artist']}", f"{c['title']} {c['artist']}")
#         if score > best_score:
#             best, best_score = c, score
#     return best, best_score
