import pytest

FirstNames = [("Joe", "Hello Joe"), ("Alex", "Hello Alex"), ("Sam", "Hello Sam")]
FirstNamesAndSureNames = [("Joe Doe", "Hello Joe Doe"), ("Alex Smith", "Hello Alex Smith"),
                          ("Sam Washington", "Hello Sam Washington")]
GummyBearJoke = [
    ("What do you call a bear with now teeth? A gummy bear!", "What do you call a bear with now teeth?\nA gummy bear!")]
Numbers_Addition = [("3+5", 8), ("6+3", 9)]


@pytest.mark.parametrize("test_input,expected_result", Numbers_Addition)
def test_param_numbers_addition(test_input, expected_result):
    print(f'Input:{test_input} Expected Result:{expected_result}')
    assert eval(test_input) == expected_result


@pytest.fixture(scope="function", params=FirstNames)
def param_first_name(request):
    return request.param


def test_first_name(param_first_name):
    (input_text, output) = param_first_name
    result = display_text(input_text)
    print(f'input:{input_text}, output: {result},expected: {output}')
    assert result == output


@pytest.fixture(scope="function", params=FirstNamesAndSureNames)
def param_test_first_and_surenames(request):
    return request.param


def test_first_name_and_surename(param_test_first_and_surenames):
    (input_text, output) = param_test_first_and_surenames
    result = display_text(input_text)
    print(f'input:{input_text}, output: {result},expected: {output}')
    assert result == output


def display_text(text):
    return f'Hello {text}'


@pytest.fixture(scope="function", params=GummyBearJoke)
def param_gummy_bear(request):
    return request.param


def test_gummy_bear_joke(param_gummy_bear):
    (input_text, output) = param_gummy_bear

    print(f'input:{input_text}, output: {output},expected: {input_text}')
    output = str(output).replace("\n", " ")
    assert input_text == output
