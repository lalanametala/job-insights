from src.counter import count_ocurrences


def test_counter():
    words = ["python", "PYTHON", "javascript", "JAVAscript"]
    path = "src/jobs.csv"
    expected_results = [1639, 1639, 122, 122]

    for i in range(len(words)):
        count_word = count_ocurrences(path, words[i])
        assert count_word == expected_results[i]
