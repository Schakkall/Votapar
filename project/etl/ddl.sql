/*
    Adicionar restrições de chaves estrangeiras
	
	Hello world, World
*/

CREATE TABLE public.tb_proposicoes(
    id bigint NOT NULL,
    ano int NOT NULL,
    numero int NOT NULL,
    sigla text
);

ALTER TABLE public.tb_proposicoes
    ADD CONSTRAINT pk_tb_proposicoes PRIMARY KEY(id);

CREATE TABLE public.tb_votacoes(
  id bigint NOT NULL,
  proposicao bigint NOT NULL,
  cod_sessao bigint NOT NULL,
  data date,
  hora time,
  obj_votacao text,
  resumo text
);

ALTER TABLE public.tb_votacoes
    ADD CONSTRAINT pk_tb_votacoes PRIMARY KEY(id);

CREATE TABLE public.tb_votos(
    id bigint NOT NULL,
    votacao bigint NOT NULL,
    ide_cadastro bigint NOT NULL,
    nome text,
    partido text,
    uf char(2),
    voto char(3)
);

ALTER TABLE public.tb_votos
    ADD CONSTRAINT pk_tb_votos PRIMARY KEY(id);


CREATE TABLE public.tb_orientacao_bancada(
    id bigint NOT NULL,
    votacao bigint NOT NULL,
    orientacao text,
    sigla text
);

ALTER TABLE public.tb_orientacao_bancada
    ADD CONSTRAINT pk_tb_orientacao_bancada PRIMARY KEY(id);
