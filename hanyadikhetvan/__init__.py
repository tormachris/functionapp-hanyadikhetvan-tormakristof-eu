from math import floor
from datetime import date
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    startdate = date(2022, 8, 29)
    currentweek = floor((date.today() - startdate).days / 7)
    return func.HttpResponse(
        str(currentweek),
        status_code=200)
