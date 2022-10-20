from src.counter import count_ocurrences


def test_counter():
    WORDS = ["python", "PYTHON", "javascript", "JAVAscript"]
    PATH = "src/jobs.csv"
    expected_results = [1639, 1639, 122, 122]

    for i in range(len(WORDS)):
        count_word = count_ocurrences(PATH, WORDS[i])
        assert count_word == expected_results[i]
