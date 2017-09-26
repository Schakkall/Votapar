/*
    Adicionar restrições de chaves estrangeiras	
*/

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


CREATE TABLE public.tb_orientacao_bancada(
    id BIGINT NOT NULL,
    votacao BIGINT NOT NULL,
    orientacao TEXT,
    sigla TEXT
);

ALTER TABLE public.tb_orientacao_bancada
    ADD CONSTRAINT pk_tb_orientacao_bancada PRIMARY KEY(id);
