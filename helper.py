from datetime import date
from datetime import datetime

def date_para_str(data: date) -> str:
    return data.strtime('%D/%M/Y')

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%D/%M/%y')

def formata_float_str(valor: float) -> str:
    return f'R$ {valor:, .2f}'
