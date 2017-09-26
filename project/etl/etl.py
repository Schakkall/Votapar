'''
    Este módulo transforma os dados em formato json em inserts sql
'''
#!/usr/bin/env python
import json

INPUT_FILE_NAME = 'votacoes_proposicoes.json'
# Logging file
LOGGING_FILE_NAME = 'output.txt'

OUTPUT_FILE = {
    'votacoes': 'votacoes.sql',
    'proposicoes': 'proposicoes.sql',
    'votos': 'votos.sql',
    'orientacao_bancada': 'orientacao_bancada.sql'}

ID = {
    'votacoes': 0,
    'proposicoes': 0,
    'votos': 0,
    'orientacao_bancada': 0}


def load_data(input_file_name):
    '''
        Returns a JSON object from a file
    '''
    with open(input_file_name, 'r') as input_file:
        stream = ''
        for line in input_file:
            stream += line
        input_file.close()
        database = json.loads(stream)
        del stream
        return database


def write_file(string, file_path):
    with open(file_path, 'w') as output_file:
        output_file.write(string)
        output_file.close()


def proposicoes_to_sql(database):
    '''
        Saves a SQL insert DML script into output_file and returns the number of elements
    '''
    sql = '''
INSERT INTO 
    public.tb_proposicoes(
           id, ano, numero, sigla)
    VALUES ({id}, {ano}, {numero}, \'{sigla}\');
'''
    votacoes_file = open(OUTPUT_FILE['votacoes'], 'w')
    votos_file = open(OUTPUT_FILE['votos'], 'w')
    orientacao_bancada_file = open(OUTPUT_FILE['orientacao_bancada'], 'w')

    ID['votacoes'], ID['votos'], ID['orientacao_bancada'] = 0, 0, 0

    with open(OUTPUT_FILE['proposicoes'], 'w') as output_file:
        ID['proposicoes'] = 0
        for prop in database:
            output_file.write(sql.format(
                id=ID['proposicoes'], ano=prop['ano'], numero=prop['numero'], sigla=prop['sigla']))
            votacoes_to_sql(prop['votacoes'], ID['proposicoes'], votacoes_file, votos_file, orientacao_bancada_file)
            ID['proposicoes'] += 1

        output_file.close()
        votacoes_file.close()
        votos_file.close()
        orientacao_bancada_file.close()
    return ID['proposicoes']


def votacoes_to_sql(database, master_id, output_file, votos_file, orientacao_bancada_file):
    '''
        Saves a SQL insert DML script into output_file and returns the number of elements
    '''
    sql = '''
INSERT INTO public.tb_votacoes(
            id, proposicao, cod_sessao, data, hora, obj_votacao, resumo)
    VALUES ({id}, {proposicao}, {cod_sessao}, \'{data}\', \'{hora}\', \'{obj_votacao}\', \'{resumo}\');
'''
    for votacao in database:
        output_file.write(sql.format(id=ID['votacoes'], proposicao=master_id, cod_sessao=votacao['cod_sessao'], data=votacao['data'],
                                     hora=votacao['hora'], obj_votacao=votacao['obj_votacao'], resumo=votacao['resumo']))
        try:
            orientacao_bancada_to_sql(
                votacao['orientacao_bancada'], ID['votacoes'], orientacao_bancada_file)
            votos_to_sql(votacao['votos'], ID['votacoes'], votos_file)
        except KeyError:
            pass
        ID['votacoes'] += 1
    return ID['votacoes']


def orientacao_bancada_to_sql(database, master_id, output_file):
    '''
        Saves a SQL insert DML script into output_file and returns de number of elements
    '''
    sql = '''
INSERT INTO public.tb_orientacao_bancada(
            id, votacao, orientacao, sigla)
    VALUES ({id}, {votacao}, \'{orientacao}\', \'{sigla}\');
'''
    for orientacao in database:
        output_file.write(sql.format(id=ID['orientacao_bancada'], votacao=master_id,
                                     orientacao=orientacao['orientacao'], sigla=orientacao['sigla']))
        ID['orientacao_bancada'] += 1
    return ID['orientacao_bancada']


def votos_to_sql(database, master_id, output_file):
    '''
        Saves a SQL insert DML script into output_file and returns de number of elements
    '''
    sql = '''
INSERT INTO public.tb_votos(
            id, votacao, ide_cadastro, nome, partido, uf, voto)
    VALUES ({id}, {votacao}, {ide_cadastro},\'{nome}\', \'{partido}\', \'{uf}\', {voto});
'''
    for votacao in database:
        output_file.write(sql.format(id=ID['votos'], votacao=master_id, ide_cadastro=votacao['ide_cadastro'], nome=votacao['nome'],
                                     partido=votacao['partido'], uf=votacao['uf'], voto=votacao['voto']))
        ID['votos'] += 1
    return ID['votos']

def load_to_database():
    '''
        TODO This function must be implemented
    '''
    pass

proposicoes_to_sql(load_data(INPUT_FILE_NAME))
