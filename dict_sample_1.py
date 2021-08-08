scores = { "A" : 60, "B": 90, "C": 40, "U": 99}
def findWorstStudent(scores):
    worstScore = None
    worstStudent = None
    for key, value in scores.items():
        if worstStudent is None or worstScore > value:
            worstStudent = key
            worstScore = value
    return worstStudent        

assert findWorstStudent(scores) == "C"
