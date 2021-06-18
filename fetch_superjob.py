import requests
from itertools import count
import os
import predict_salary


def get_all_vacancies(language):
    vacancies = []
    for page in count(0):
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {
            "X-Api-App-Id": os.getenv("SUPERJOB_APP_ID")
        }
        params = {
            "town": "4",
            "catalogues": "48",
            "keyword": f"{language}",
            "page": f"{page}",
            "count": "100"
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        vacancies += response.json().get("objects")
        if not response.json().get("more"):
            break
    vacancies_found = response.json().get("total")
    return (vacancies, vacancies_found)


def get_all_vacancies_findings(languages):
    all_vacancies_findings = []
    for language in languages:
        vacancies, vacancies_found = get_all_vacancies(language)
        vacancies_processed = 0
        salaries_sum = 0
        for vacancy in vacancies:
            if vacancy["currency"] == "rub":
                predicted_salary = predict_salary.predict_rub_salary(vacancy["payment_from"], vacancy["payment_to"])
                if predicted_salary:
                    salaries_sum += predicted_salary
                    vacancies_processed += 1
                if vacancies_processed:
                    average_salary = int(salaries_sum/vacancies_processed)
        vacancy_findings = {
            language: {
                "vacancies_found": vacancies_found,
                "vacancies_processed": vacancies_processed,
                "average_salary": average_salary
                }
            }

        all_vacancies_findings.append(vacancy_findings)
    return all_vacancies_findings