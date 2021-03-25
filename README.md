# monitoramento_semanal_automatizado
Projeto de automação de um monitoramento semanal de equipamentos.

Este projeto utilizará uma tabela em excel extraída de um banco de dados manualmente, a princípio, e irá tratar os dados 
gerando relatórios úteis para determinar se um equipamento precisa ou não de manutenção.

O arquivo alarmes serão utilizados dentro do arquivo de excel para criar uma aba para cada equipamento exibindo as
linhas de cada alarme juntamente com os dados de data, hora inicial, hora final, tipo de alarme, duração e uma possível 
especificação do erro.

O arquivo de disponibilidade serão utilizados para extrair a disponibilidade de cada equipamento verificando se os 
arquivos são transmitidos a cada 5 minutos e a cada 15 minutos.

O arquivo monitoramento é um exemplo de como deverá ficar o arquivo ao final desta automação.

Versão
```console
Python 3 .venv
```
