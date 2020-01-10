from dimensions import DIMENSIONS
import random


def get_combinations(dimensions):
    return [(dimensions[i]['name'], dimensions[j]['name'])
            for i in range(len(dimensions) - 1)
            for j in range(i + 1, len(dimensions))] * 2


def get_shuffled_questions(dimensions):
    questions = {d['name']: d['answers'] for d in dimensions}
    [random.shuffle(questions[q]) for q in questions]
    return questions


def get_assessment(dimensions):
    result = []
    possible_combinations = get_combinations(dimensions)
    questions = get_shuffled_questions(dimensions)
    for (name_1, name_2) in possible_combinations:
        result.append(((name_1, questions[name_1][0]), (name_2, questions[name_2][0])))
        questions[name_1] = questions[name_1][1:]
        questions[name_2] = questions[name_2][1:]
    random.shuffle(result)
    return result


def run_assessment(dimensions):
    assessment = get_assessment(dimensions)
    result = {d['name']: 0 for d in dimensions}
    for q in assessment:
        print('Please select (1/2):')
        print('1', q[0][1])
        print('2', q[1][1])
        response = ''
        while response not in ['1', '2']:
            response = input()
        result[q[int(response) - 1][0]] += 1
    return result


if __name__ == '__main__':
    print('Assessment result: ', run_assessment(DIMENSIONS))
