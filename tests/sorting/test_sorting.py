from src.sorting import sort_by
from src.jobs import read
from src.insights import get_min_salary, get_max_salary


def test_sort_by_criteria():
    path = "src/jobs.csv"
    all_jobs = read(path)

    sort_by(all_jobs, "min_salary")
    expected = get_min_salary(path)
    result = all_jobs[0]["min_salary"]
    assert result == str(expected)

    sort_by(all_jobs, "max_salary")
    expected = get_max_salary(path)
    result = all_jobs[0]["max_salary"]
    assert result == str(expected)
