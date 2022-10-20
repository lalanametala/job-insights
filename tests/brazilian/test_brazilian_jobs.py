from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_english = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in dict_english:
        assert job.get("titulo") is None
        assert job.get("salario") is None
        assert job.get("tipo") is None
        assert job.get("title") is not None
        assert job.get("salary") is not None
        assert job.get("type") is not None
