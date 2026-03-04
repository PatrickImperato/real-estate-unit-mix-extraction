def score_one(gold: dict, pred: dict) -> dict:
    total_exact = int(gold.get("total_units") == pred.get("total_units"))
    gmix = {(u["beds"], float(u["baths"])): u["count"] for u in gold.get("unit_mix", [])}
    pmix = {(u["beds"], float(u["baths"])): u["count"] for u in pred.get("unit_mix", [])}
    mix_exact = int(gmix == pmix)
    overlap = sum(1 for k,v in gmix.items() if pmix.get(k) == v)
    overlap_rate = overlap / max(1, len(gmix))
    return {"total_exact": total_exact, "mix_exact": mix_exact, "mix_overlap_rate": overlap_rate}
