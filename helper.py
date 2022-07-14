from datetime import date
from datetime import datetime

# Especifição da data para a formatação PT-BR e de date para string

def date_para_str(data: date) -> str:
    return data.strtime('%d/%m/Y')

# Formatação de string para Date

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

# De float para string

def formata_float_str(valor: float) -> str:
    return f'R$ {valor:, .2f}'
