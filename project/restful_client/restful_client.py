"""
    This module consumes the Camara's Web API to get it in SQL DML Insert Scripts
"""
import json
import requests

PAGE_SIZE = 100
URL_DEPUTADOS = "https://dadosabertos.camara.leg.br/api/v2/deputados?pagina=1&itens={pagesize}".format(pagesize=PAGE_SIZE)
URL_PARTIDOS = "https://dadosabertos.camara.leg.br/api/v2/partidos?pagina=1&itens={pagesize}".format(pagesize=PAGE_SIZE)
URL_BLOCOS = "https://dadosabertos.camara.leg.br/api/v2/blocos?pagina=1&itens={pagesize}".format(pagesize=PAGE_SIZE)
URL_LEGISLATURAS = "https://dadosabertos.camara.leg.br/api/v2/legislaturas?pagina=1&itens={pagesize}".format(pagesize=PAGE_SIZE)
URL_PROPOSICOES = "https://dadosabertos.camara.leg.br/api/v2/proposicoes?ordem=ASC&ordenarPor=id&itens={pagesize}".format(pagesize=PAGE_SIZE)

def request(url):
    """
        Returns a JSON object from a request in a REST API
    """
    response = requests.get(url)
    if (response.ok):
        jobject = json.loads(response.content)
    else:
        response.raise_for_status()
    return jobject

def dump_it(jobject, output_file):
    if len(jobject['dados']) == PAGE_SIZE:
        output_file.write(str(jobject['dados']))
        next_url = jobject['links'][1]['href']
        dump_it(request(next_url), output_file)
    elif len(jobject['dados']) < PAGE_SIZE:
        output_file.write(str(jobject['dados']))
        pass


with open('deputados.json', 'w') as deputados_file:
    dump_it(request(URL_DEPUTADOS), deputados_file)
    deputados_file.close()

with open('partidos.json', 'w') as partidos_file:
    dump_it(request(URL_PARTIDOS), partidos_file)
    deputados_file.close()

with open('blocos.json', 'w') as blocos_file:
    dump_it(request(URL_BLOCOS), blocos_file)
    deputados_file.close()    

with open('legislaturas.json', 'w') as partidos_file:
    dump_it(request(URL_LEGISLATURAS), partidos_file)
    deputados_file.close()

with open('proposicoes.json', 'w') as blocos_file:
    dump_it(request(URL_PROPOSICOES), blocos_file)
    deputados_file.close()        
