import logging
from re import U
import re
from . import extract_domain

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    url = req_body.get("url")
    if url:
        domain = extract_domain.extract_domain(url)
        return func.HttpResponse(domain)