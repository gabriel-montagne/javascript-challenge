from dimensions import DIMENSIONS


def test_list_structure():
    actual_list_structure = set((type(elem).__name__ for elem in DIMENSIONS))
    expected_list_structure = {'dict'}
    assert actual_list_structure == expected_list_structure


def test_element_structure():
    actual_element_keys = set(k for elem in DIMENSIONS for k in elem)
    expected_element_keys = {'name', 'answers'}
    assert actual_element_keys == expected_element_keys


def test_number_of_answers_per_dimension():
    n = len(DIMENSIONS)
    actual_number = set(len(elem['answers']) for elem in DIMENSIONS)
    expected_number = {2 * (n - 1)}
    assert actual_number == expected_number
