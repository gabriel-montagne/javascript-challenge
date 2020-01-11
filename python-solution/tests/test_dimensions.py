from dimensions import DIMENSIONS


def test_list_structure():
    """
    1. Test DIMENSIONS is a list of dictionaries
    2. Test the number of dimensions IMPORTANT: If test is to be restructured on a different number
    of dimension this is the only test that should be corrected
    """
    assert type(DIMENSIONS).__name__ == 'list'
    actual_list_structure = set((type(elem).__name__ for elem in DIMENSIONS))
    expected_list_structure = {'dict'}
    assert actual_list_structure == expected_list_structure
    assert len(DIMENSIONS) == 6


def test_element_structure():
    """
    1. Test that all dictionaries have proper keys
    """
    actual_element_keys = set(k for elem in DIMENSIONS for k in elem)
    expected_element_keys = {'name', 'answers'}
    assert actual_element_keys == expected_element_keys


def test_number_of_answers_per_dimension():
    """
    1. Test the correlation between the number of dimensions and the number of answers
    """
    n = len(DIMENSIONS)
    actual_number = set(len(elem['answers']) for elem in DIMENSIONS)
    expected_number = {2 * (n - 1)}
    assert actual_number == expected_number
