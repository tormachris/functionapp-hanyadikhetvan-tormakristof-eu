from math import floor
from datetime import date
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    startdate = date(2022, 2, 6)
    return func.HttpResponse(
        floor((date.today() - startdate).days / 7),
        status_code=200)
