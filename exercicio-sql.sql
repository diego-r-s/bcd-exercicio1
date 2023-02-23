use application;
select *from cliente;
describe cliente;
select *from consultorinvestimento;
describe fundoinvestimento;

insert into consultorinvestimento
(nomeConsultor, percentualComissao)
values ("João Félix", 15.7), ("Joana Maria", 16);



insert into fundoinvestimento
(nomeComlFundo, codTipoFundoFK, ativo)
values ("CDB 2023", 2, "N"), ("AÇÕES 2023", 1, "A");