import logging
import azure.functions as func
from .cpf_validator import validate_cpf, save_cpf, get_cpf

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cpf = req.params.get('cpf')
    action = req.params.get('action')

    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')
            action = req_body.get('action')

    if action == 'validate':
        if cpf and validate_cpf(cpf):
            save_cpf(cpf)
            return func.HttpResponse(f"CPF {cpf} is valid and saved.")
        else:
            return func.HttpResponse("Invalid CPF.", status_code=400)
    elif action == 'get':
        if cpf:
            result = get_cpf(cpf)
            if result:
                return func.HttpResponse(f"CPF {cpf} found: {result}")
            else:
                return func.HttpResponse("CPF not found.", status_code=404)
    else:
        return func.HttpResponse("Invalid action.", status_code=400)
