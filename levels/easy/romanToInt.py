def romanToInt(s: str) -> int:
    conversions = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    comparisons = {
        "I":{"V","X"},
        "X":{"L","C"},
        "C":{"D","M"}
    }
    
    total = 0
    for i, v in enumerate(s):
        nextv = ''
        if i+1 < len(s):
            nextv = s[i+1]
        if v in {"I","X","C"} and nextv in comparisons[v]:
            total -= conversions[v]
        else:
            total += conversions[v]

    return total