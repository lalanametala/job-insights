from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    unique_jobs = set()

    for job in all_jobs:
        if job["job_type"] is not None:
            unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = read(path)
    unique_industries = set()

    for job in all_jobs:
        if job["industry"] != '':
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    all_jobs = read(path)
    max_salaries = []
    for job in all_jobs:
        if job["max_salary"].isdigit():
            max_salaries.append(int(job["max_salary"]))
    return max(max_salaries)


def get_min_salary(path):
    all_jobs = read(path)
    min_salaries = []
    for job in all_jobs:
        if job["min_salary"].isdigit():
            min_salaries.append(int(job["min_salary"]))
    return min(min_salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
