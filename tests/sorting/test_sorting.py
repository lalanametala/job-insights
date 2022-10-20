from src.sorting import sort_by
from src.jobs import read
from src.insights import get_min_salary, get_max_salary


def test_sort_by_criteria():
    path = "src/jobs.csv"
    all_jobs = read(path)

    criteria_keys = {
        "max_salary": get_max_salary,
        "min_salary": get_min_salary,
    }

    for key in criteria_keys:
        sort_by(all_jobs, key)
        expected = criteria_keys[key](path)
        assert all_jobs[0] == str(expected)
