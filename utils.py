import json

def load_candidates():
    with open("candidates.json", "r", encoding="UTF-8") as file:
        return json.load(file)

def get_candidates_all():
    return load_candidates()

def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'

def get_candidates_by_skill(skill):
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].split(', ')
        if skill in skills:
            result.append(candidate)
    return result