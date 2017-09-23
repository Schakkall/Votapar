import json

def transform_deputados(input_file_name, output_file_name):
    sql = '''
    INSERT INTO 
        public.tb_deputados (
            id, uri, nome, siglaPartido, uriPartido, 
            siglaUf, idLegislatura, urlFoto
        ) VALUES (
            {id}, \'{uri}\', \'{nome}\', \'{siglaPartido}\', \'{uriPartido}\'
            \'{siglaUf}\', \'{idLegislatura}\', \'{urlFoto}\'
        );

'''    
    output_file = open(output_file_name, 'w')
    with open(input_file_name, 'r') as input_file:
        stream = input_file.read()
        db = json.loads(stream)
        for deputado in db['data']:    
            output_file.write(
                sql.format(id=deputado['id'], uri=deputado['uri'], nome=deputado['nome'], 
                siglaPartido=deputado['siglaPartido'], uriPartido=deputado['uriPartido'],
                siglaUf=deputado['siglaUf'], idLegislatura=deputado['idLegislatura'], 
                urlFoto=deputado['urlFoto']))

def transform_proposicoes(input_file_name, output_file_name):
    sql = '''
    INSERT INTO 
        public.tb_proposicoes (
            id, uri, nome, siglaPartido, uriPartido, 
            siglaUf, idLegislatura, urlFoto
        ) VALUES (
            {id}, \'{uri}\', \'{nome}\', \'{siglaPartido}\', \'{uriPartido}\'
            \'{siglaUf}\', \'{idLegislatura}\', \'{urlFoto}\'
        );

'''    
    output_file = open(output_file_name, 'w')
    with open(input_file_name, 'r') as input_file:
        stream = input_file.read()
        db = json.loads(stream)
        for deputado in db['data']:    
            output_file.write(
                sql.format(id=deputado['id'], uri=deputado['uri'], nome=deputado['nome'], 
                siglaPartido=deputado['siglaPartido'], uriPartido=deputado['uriPartido'],
                siglaUf=deputado['siglaUf'], idLegislatura=deputado['idLegislatura'], 
                urlFoto=deputado['urlFoto']))
                

transform_deputados('deputados.json', 'deputados.sql')        