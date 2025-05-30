# flows/main_flow.py

from prefect import flow
from tasks.extract import extract_offers


@flow
def linkedin_etl_flow():
    url = "https://www.linkedin.com/jobs/search/?keywords=python"  # Cambiar según necesidad

    raw_data = extract_offers(url)
 

if __name__ == "__main__":
    linkedin_etl_flow()
