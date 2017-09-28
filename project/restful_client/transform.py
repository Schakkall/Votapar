import json

def transform_deputados(input_file_name, output_file_name):
    sql = '''
INSERT INTO public.tb_deputados(
            id, uri, nome, siglapartido, uripartido, siglauf, idlegislatura, urlfoto)
    VALUES ({id}, \'{uri}\', \'{nome}\', 
           \'{siglaPartido}\', \'{uriPartido}\',
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
INSERT INTO public.tb_det_proposicoes(
            id, cod_orgao_origem, num_legislatura_apresen, num_legislatura_lei, 
            dat_inicio_legislatura_vet_total, nom_partido_politico, dat_veto_total, 
            nom_uf, des_tipo_proposicao, des_completa, cod_tipo_norma_juridica_origem, 
            sig_uf, dat_fim_legislatura_lei, cod_proposicao_origem, dat_fim_legislatura_vet_total, 
            des_ativo_tipo_proposicao, des_tipo_sessao_legislativa_vet_total, 
            nom_orgao, cod_tipo_sessao_legislativa_vet_total, des_apelido_orgao, 
            datapresentacaoproposicao, des_tipo_autor, cod_sexo, dat_inicio_sessao_legislativa_vet_total, 
            ind_ativo_orgao, cod_tipo_parlamentar, des_tipo_norma_juridica, 
            des_tipo_sessao_legislativa_apresen, dattransfproposicaolei, 
            dat_final_recesso_lei, areas_tematicas_apresentacao, dat_final_recesso_vet_total, 
            dat_fim_sessao_legislativa_vet_total, des_tipo_sessao_legislativa_lei, 
            dat_inicial_recesso_apresen, ano_proposicao, num_legislatura_vet_total, 
            tex_regiao_geografica_autor, dat_inicio_legislatura_lei, num_sessao_legislativa_apresen, 
            dat_inicial_recesso_lei, dat_fim_sessao_legislativa_apresen, 
            sig_norma_juridica, dat_inicio_sessao_legislativa_lei, des_tipo_parlamentar, 
            nom_proposicao, des_ativo_orgao, cod_partido_politico, nom_civil_parlamentar, 
            sig_tipo_proposicao, cod_tipo_sessao_legislativa_apresen, dat_inicio_sessao_legislativa_apresen, 
            cod_parlamentar_origem, dat_fim_sessao_legislativa_lei, num_sessao_legislativa_vet_total, 
            des_situacao_proposicao, cod_tipo_autor_origem, num_sessao_legislativa_lei, 
            dat_fim_legislatura_apresen, sig_partido_politico, ind_ativo_tipo_proposicao, 
            dat_inicio_legislatura_apresen, num_proposicao, cod_tipo_sessao_legislativa_lei, 
            nom_parlamentar, dat_final_recesso_apresen, dat_inicial_recesso_vet_total)
    VALUES (            
            {id}, \'{cod_orgao_origem}\', \'{num_legislatura_apresen}\', \'{num_legislatura_lei}\', 
            \'{dat_inicio_legislatura_vet_total}\', \'{nom_partido_politico}\', \'{dat_veto_total}\', 
            \'{nom_uf}\', \'{des_tipo_proposicao}\', \'{des_completa}\', \'{cod_tipo_norma_juridica_origem}\', 
            \'{sig_uf}\', \'{dat_fim_legislatura_lei}\', \'{cod_proposicao_origem}\', \'{dat_fim_legislatura_vet_total}\', 
            \'{des_ativo_tipo_proposicao}\', \'{des_tipo_sessao_legislativa_vet_total}\', 
            \'{nom_orgao}\', \'{cod_tipo_sessao_legislativa_vet_total}\', \'{des_apelido_orgao}\', 
            \'{datapresentacaoproposicao}\', \'{des_tipo_autor}\', \'{cod_sexo}\', \'{dat_inicio_sessao_legislativa_vet_total}\', 
            \'{ind_ativo_orgao}\', \'{cod_tipo_parlamentar}\', \'{des_tipo_norma_juridica}\', 
            \'{des_tipo_sessao_legislativa_apresen}\', \'{dattransfproposicaolei}\', 
            \'{dat_final_recesso_lei}\', \'{areas_tematicas_apresentacao}\', \'{dat_final_recesso_vet_total}\', 
            \'{dat_fim_sessao_legislativa_vet_total}\', \'{des_tipo_sessao_legislativa_lei}\', 
            \'{dat_inicial_recesso_apresen}\', \'{ano_proposicao}\', \'{num_legislatura_vet_total}\', 
            \'{tex_regiao_geografica_autor}\', \'{dat_inicio_legislatura_lei}\', \'{num_sessao_legislativa_apresen}\', 
            \'{dat_inicial_recesso_lei}\', \'{dat_fim_sessao_legislativa_apresen}\', 
            \'{sig_norma_juridica}\', \'{dat_inicio_sessao_legislativa_lei}\', \'{des_tipo_parlamentar}\', 
            \'{nom_proposicao}\', \'{des_ativo_orgao}\', \'{cod_partido_politico}\', \'{nom_civil_parlamentar}\', 
            \'{sig_tipo_proposicao}\', \'{cod_tipo_sessao_legislativa_apresen}\', \'{dat_inicio_sessao_legislativa_apresen}\', 
            \'{cod_parlamentar_origem}\', \'{dat_fim_sessao_legislativa_lei}\', \'{num_sessao_legislativa_vet_total}\', 
            \'{des_situacao_proposicao}\', \'{cod_tipo_autor_origem}\', \'{num_sessao_legislativa_lei}\', 
            \'{dat_fim_legislatura_apresen}\', \'{sig_partido_politico}\', \'{ind_ativo_tipo_proposicao}\', 
            \'{dat_inicio_legislatura_apresen}\', \'{num_proposicao}\', \'{cod_tipo_sessao_legislativa_lei}\', 
            \'{nom_parlamentar}\', \'{dat_final_recesso_apresen}\', \'{dat_inicial_recesso_vet_total}\');
'''    
    output_file = open(output_file_name, 'w')
    with open(input_file_name, 'r') as input_file:
        stream = input_file.read()
        db = json.loads(stream)
        i = 0
        for prop in db['data']:    
            output_file.write(
                sql.format(                
                    id = i,
                    cod_orgao_origem = prop['COD_ORGAO_ORIGEM'],
                    num_legislatura_apresen = prop['NUM_LEGISLATURA_APRESEN'],
                    num_legislatura_lei  = prop['NUM_LEGISLATURA_LEI'],
                    dat_inicio_legislatura_vet_total = prop['DAT_INICIO_LEGISLATURA_VET_TOTAL'],
                    nom_partido_politico  = prop['NOM_PARTIDO_POLITICO'],
                    dat_veto_total = prop['DAT_VETO_TOTAL'],
                    nom_uf = prop['NOM_UF'],
                    des_tipo_proposicao = prop['DES_TIPO_PROPOSICAO'],
                    des_completa = prop['DES_COMPLETA'],
                    cod_tipo_norma_juridica_origem = prop['COD_TIPO_NORMA_JURIDICA_ORIGEM'],
                    sig_uf = prop['SIG_UF'],
                    dat_fim_legislatura_lei  = prop['DAT_FIM_LEGISLATURA_LEI'] ,
                    cod_proposicao_origem  = prop['COD_PROPOSICAO_ORIGEM'],
                    dat_fim_legislatura_vet_total = prop['DAT_FIM_LEGISLATURA_VET_TOTAL'],
                    des_ativo_tipo_proposicao  = prop['DES_ATIVO_TIPO_PROPOSICAO'] ,
                    des_tipo_sessao_legislativa_vet_total = prop['DES_TIPO_SESSAO_LEGISLATIVA_VET_TOTAL'],
                    nom_orgao = prop['NOM_ORGAO'],
                    cod_tipo_sessao_legislativa_vet_total = prop['COD_TIPO_SESSAO_LEGISLATIVA_VET_TOTAL'],
                    des_apelido_orgao = prop['DES_APELIDO_ORGAO'],
                    datapresentacaoproposicao  = prop['DATAPRESENTACAOPROPOSICAO'] ,
                    des_tipo_autor  = prop['DES_TIPO_AUTOR'],
                    cod_sexo  = prop['COD_SEXO'],
                    dat_inicio_sessao_legislativa_vet_total = prop['DAT_INICIO_SESSAO_LEGISLATIVA_VET_TOTAL'],
                    ind_ativo_orgao = prop['IND_ATIVO_ORGAO'],
                    cod_tipo_parlamentar = prop['COD_TIPO_PARLAMENTAR'],
                    des_tipo_norma_juridica = prop['DES_TIPO_NORMA_JURIDICA'],
                    des_tipo_sessao_legislativa_apresen = prop['DES_TIPO_SESSAO_LEGISLATIVA_APRESEN'],
                    dattransfproposicaolei  = prop['DATTRANSFPROPOSICAOLEI'] ,
                    dat_final_recesso_lei  = prop['DAT_FINAL_RECESSO_LEI'] ,
                    areas_tematicas_apresentacao = prop['AREAS_TEMATICAS_APRESENTACAO'],
                    dat_final_recesso_vet_total  = prop['DAT_FINAL_RECESSO_VET_TOTAL'],
                    dat_fim_sessao_legislativa_vet_total = prop['DAT_FIM_SESSAO_LEGISLATIVA_VET_TOTAL'],
                    des_tipo_sessao_legislativa_lei  = prop['DES_TIPO_SESSAO_LEGISLATIVA_LEI'],
                    dat_inicial_recesso_apresen  = prop['DAT_INICIAL_RECESSO_APRESEN'],
                    ano_proposicao  = prop['ANO_PROPOSICAO'] ,
                    num_legislatura_vet_total = prop['NUM_LEGISLATURA_VET_TOTAL'],
                    tex_regiao_geografica_autor  = prop['TEX_REGIAO_GEOGRAFICA_AUTOR'],
                    dat_inicio_legislatura_lei  = prop['DAT_INICIO_LEGISLATURA_LEI'],
                    num_sessao_legislativa_apresen  = prop['NUM_SESSAO_LEGISLATIVA_APRESEN'],
                    dat_inicial_recesso_lei  = prop['DAT_INICIAL_RECESSO_LEI'],
                    dat_fim_sessao_legislativa_apresen = prop['DAT_FIM_SESSAO_LEGISLATIVA_APRESEN'],
                    sig_norma_juridica  = prop['SIG_NORMA_JURIDICA'],
                    dat_inicio_sessao_legislativa_lei = prop['DAT_INICIO_SESSAO_LEGISLATIVA_LEI'],
                    des_tipo_parlamentar  = prop['DES_TIPO_PARLAMENTAR'],
                    nom_proposicao  = prop['NOM_PROPOSICAO'],
                    des_ativo_orgao  = prop['DES_ATIVO_ORGAO'],
                    cod_partido_politico = prop['COD_PARTIDO_POLITICO'],
                    nom_civil_parlamentar = prop['NOM_CIVIL_PARLAMENTAR'],
                    sig_tipo_proposicao  = prop['SIG_TIPO_PROPOSICAO'],
                    cod_tipo_sessao_legislativa_apresen  = prop['COD_TIPO_SESSAO_LEGISLATIVA_APRESEN'],
                    dat_inicio_sessao_legislativa_apresen = prop['DAT_INICIO_SESSAO_LEGISLATIVA_APRESEN'],
                    cod_parlamentar_origem = prop['COD_PARLAMENTAR_ORIGEM'],
                    dat_fim_sessao_legislativa_lei = prop['DAT_FIM_SESSAO_LEGISLATIVA_LEI'],
                    num_sessao_legislativa_vet_total = prop['NUM_SESSAO_LEGISLATIVA_VET_TOTAL'],
                    des_situacao_proposicao  = prop['DES_SITUACAO_PROPOSICAO'],
                    cod_tipo_autor_origem = prop['COD_TIPO_AUTOR_ORIGEM'],
                    num_sessao_legislativa_lei  = prop['NUM_SESSAO_LEGISLATIVA_LEI'],
                    dat_fim_legislatura_apresen  = prop['DAT_FIM_LEGISLATURA_APRESEN'],
                    sig_partido_politico  = prop['SIG_PARTIDO_POLITICO'],
                    ind_ativo_tipo_proposicao  = prop['IND_ATIVO_TIPO_PROPOSICAO'],
                    dat_inicio_legislatura_apresen = prop['DAT_INICIO_LEGISLATURA_APRESEN'],
                    num_proposicao  = prop['NUM_PROPOSICAO'],
                    cod_tipo_sessao_legislativa_lei = prop['COD_TIPO_SESSAO_LEGISLATIVA_LEI'],
                    nom_parlamentar  = prop['NOM_PARLAMENTAR'],
                    dat_final_recesso_apresen  = prop['DAT_FINAL_RECESSO_APRESEN'],
                    dat_inicial_recesso_vet_total  = prop['DAT_INICIAL_RECESSO_VET_TOTAL']))
            i += 1
                

#transform_deputados('deputados.json', 'deputados.sql')        
transform_proposicoes('proposicoes.json', 'proposicoes.sql')        