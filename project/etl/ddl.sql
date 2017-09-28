CREATE TABLE public.tb_deputados(
    id BIGINT NOT NULL,
    uri TEXT,
    nome TEXT,
    siglaPartido TEXT,
    uriPartido TEXT,
    siglaUf CHAR(2),
    idLegislatura TEXT,
    urlFoto TEXT
);

ALTER TABLE public.tb_deputados
    ADD CONSTRAINT pk_tb_deputados PRIMARY KEY(id);


CREATE TABLE public.tb_proposicoes(
    id BIGINT NOT NULL,
    ano INT NOT NULL,
    numero INT NOT NULL,
    sigla TEXT
);

ALTER TABLE public.tb_proposicoes
    ADD CONSTRAINT pk_tb_proposicoes PRIMARY KEY(id);

CREATE TABLE public.tb_votacoes(
  id BIGINT NOT NULL,
  proposicao BIGINT NOT NULL,
  cod_sessao BIGINT NOT NULL,
  data DATE,
  hora TIME,
  obj_votacao TEXT,
  resumo TEXT
);

ALTER TABLE public.tb_votacoes
    ADD CONSTRAINT pk_tb_votacoes PRIMARY KEY(id);

ALTER TABLE public.tb_votacoes
    ADD CONSTRAINT fK_proposicao 
        FOREIGN KEY (proposicao) 
            REFERENCES public.tb_proposicoes(id);
    

CREATE TABLE public.tb_votos(
    id BIGINT NOT NULL,
    votacao BIGINT NOT NULL,
    ide_cadastro BIGINT NOT NULL,
    nome TEXT,
    partido TEXT,
    uf CHAR(2),
    voto CHAR(3)
);

ALTER TABLE public.tb_votos
    ADD CONSTRAINT pk_tb_votos PRIMARY KEY(id);

ALTER TABLE public.tb_votos
    ADD CONSTRAINT fk_votacao
        FOREIGN KEY (votacao) 
            REFERENCES public.tb_votacoes(id);


CREATE TABLE public.tb_orientacao_bancada(
    id BIGINT NOT NULL,
    votacao BIGINT NOT NULL,
    orientacao TEXT,
    sigla TEXT
);

ALTER TABLE public.tb_orientacao_bancada
    ADD CONSTRAINT pk_tb_orientacao_bancada PRIMARY KEY(id);

ALTER TABLE public.tb_orientacao_bancada
    ADD CONSTRAINT fk_votacao
        FOREIGN KEY (votacao) 
            REFERENCES public.tb_orientacao_bancada(id);

CREATE TABLE public.tb_det_proposicoes(
    id BIGINT NOT NULL,
    cod_orgao_origem TEXT,
    num_legislatura_apresen TEXT,
    num_legislatura_lei TEXT, 
    dat_inicio_legislatura_vet_total TEXT,
    nom_partido_politico TEXT, 
    dat_veto_total TEXT,
    nom_uf TEXT,
    des_tipo_proposicao TEXT,
    des_completa TEXT,
    cod_tipo_norma_juridica_origem TEXT,
    sig_uf TEXT,
    dat_fim_legislatura_lei TEXT, 
    cod_proposicao_origem TEXT, 
    dat_fim_legislatura_vet_total TEXT,
    des_ativo_tipo_proposicao TEXT, 
    des_tipo_sessao_legislativa_vet_total TEXT,
    nom_orgao TEXT,
    cod_tipo_sessao_legislativa_vet_total TEXT,
    des_apelido_orgao TEXT,
    datapresentacaoproposicao TEXT, 
    des_tipo_autor TEXT, 
    cod_sexo TEXT, 
    dat_inicio_sessao_legislativa_vet_total TEXT,
    ind_ativo_orgao TEXT,
    cod_tipo_parlamentar TEXT,
    des_tipo_norma_juridica TEXT,
    des_tipo_sessao_legislativa_apresen TEXT,
    dattransfproposicaolei TEXT, 
    dat_final_recesso_lei TEXT, 
    areas_tematicas_apresentacao TEXT,
    dat_final_recesso_vet_total TEXT, 
    dat_fim_sessao_legislativa_vet_total TEXT,
    des_tipo_sessao_legislativa_lei TEXT, 
    dat_inicial_recesso_apresen TEXT, 
    ano_proposicao TEXT, 
    num_legislatura_vet_total TEXT,
    tex_regiao_geografica_autor TEXT, 
    dat_inicio_legislatura_lei TEXT, 
    num_sessao_legislativa_apresen TEXT, 
    dat_inicial_recesso_lei TEXT, 
    dat_fim_sessao_legislativa_apresen TEXT,
    sig_norma_juridica TEXT, 
    dat_inicio_sessao_legislativa_lei TEXT,
    des_tipo_parlamentar TEXT, 
    nom_proposicao TEXT, 
    des_ativo_orgao TEXT, 
    cod_partido_politico TEXT,
    nom_civil_parlamentar TEXT,
    sig_tipo_proposicao TEXT, 
    cod_tipo_sessao_legislativa_apresen TEXT, 
    dat_inicio_sessao_legislativa_apresen TEXT,
    cod_parlamentar_origem TEXT,
    dat_fim_sessao_legislativa_lei TEXT,
    num_sessao_legislativa_vet_total TEXT,
    des_situacao_proposicao TEXT, 
    cod_tipo_autor_origem TEXT,
    num_sessao_legislativa_lei TEXT, 
    dat_fim_legislatura_apresen TEXT, 
    sig_partido_politico TEXT, 
    ind_ativo_tipo_proposicao TEXT, 
    dat_inicio_legislatura_apresen TEXT,
    num_proposicao TEXT, 
    cod_tipo_sessao_legislativa_lei TEXT,
    nom_parlamentar TEXT, 
    dat_final_recesso_apresen TEXT, 
    dat_inicial_recesso_vet_total TEXT	
);

ALTER TABLE public.tb_det_proposicoes
    ADD CONSTRAINT pk_tb_det_proposicoes PRIMARY KEY(id);
