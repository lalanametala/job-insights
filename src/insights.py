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
    if (
        job.get("min_salary") is None
        or job.get("max_salary") is None
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or type(salary) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            print("One or more parameters are incorrect. Unable to add job.")
    return filtered_jobs
