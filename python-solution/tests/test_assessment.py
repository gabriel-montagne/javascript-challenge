import random
from collections import defaultdict

import assessment
from assessment import get_combinations, get_assessment, run_assessment

N = 5
TEST_DIMENSIONS = [{
                    'name': 'dimension-%d' % i,
                    'answers': ['answer-%d-%d' % (i, j) for j in range(2*(N - 1))]
                    }
                   for i in range(N)]


def test_number_of_combinations():
    """
    Test if all the dimension combinations are returned
    """
    dim_length = len(TEST_DIMENSIONS)
    assert dim_length * (dim_length - 1) == len(get_combinations(TEST_DIMENSIONS))


def test_assessment_structure():
    """
    1. Test if assessment has the expected number of pairs of questions
    2. Test if all the pairs have 2 questions
    """
    expected_number = N * (N - 1)
    assessment = get_assessment(TEST_DIMENSIONS)
    actual_number = len(assessment)
    assert expected_number == actual_number
    expected_number_of_questions_per_elem = {2}
    actual_number_of_questions_per_elem = set(len(elem) for elem in assessment)
    assert expected_number_of_questions_per_elem == actual_number_of_questions_per_elem


def test_assessment_questions():
    """
    1. Test if all the questions in the assessment are from the dimension answers
    2. If all the dimensions answers are in the assessment
    """
    assessment = get_assessment(TEST_DIMENSIONS)
    actual_dimensions = defaultdict(list)
    for q1, q2 in assessment:
        actual_dimensions[q1[0]].append(q1[1])
        actual_dimensions[q2[0]].append(q2[1])
    expected_dimensions = {d['name']: d['answers'] for d in TEST_DIMENSIONS}
    for key in actual_dimensions:
        assert [d for d in actual_dimensions[key] if d in expected_dimensions[key]] == actual_dimensions[key]
        assert [d for d in expected_dimensions[key] if d in actual_dimensions[key]] == expected_dimensions[key]


def test_result():
    """
    1. Test if the result is a dictionary
    2. If all the TEST_DIMENSIONS names are all in the result
    3. If the sum of the values is equal with the number of combinations
    """
    def mock_input():
        return random.choice(['1', '2'])
    assessment.input = mock_input
    result = run_assessment(TEST_DIMENSIONS)
    assert type(result).__name__ == 'dict'
    actual_dimensions = [ad['name'] for ad in TEST_DIMENSIONS]
    assert [ed for ed in result if ed in actual_dimensions] == [ed for ed in result]
    assert [ed for ed in actual_dimensions if ed in result] == [ed for ed in actual_dimensions]
    dimensions_len = len(TEST_DIMENSIONS)
    assert sum([v for _, v in result.items()]) == dimensions_len * (dimensions_len - 1)
