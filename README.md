# MyWhois

Esta é uma simples ferramenta que nos auxilia na coleta de informações sobre um determinado alvo.
Dados que podem ser retornados:<br>
IP<br>
País<br>
Região<br>
Cidade<br>
Codigo portal<br>
ASN<br>
AS<br>
Verifica Se é um proxy<br>

## Configuração

Ela utiliza atualmente a API do IP2Location, na qual poderá ser adquirida a sua e configurada em seu ambiente com o comando:
`export TOKEN=seu_token_aqui`

## Utilização

Consulta direta a um endereço IP<br>
`python3 mywhois.py -i 192.168.1.1`

Consulta direta a um dominio<br>
`python3 mywhois.py -d exemplo.com`

Consulta atraves de arquivo contendo endereço IP<br>
`python3 mywhois.py -iF ip.txt`

Consulta atraves de arquivo contendo dominios/subdominios<br>
`python3 mywhois.py -dF dominios.txt`


Consulta atraves de arquivo contendo dominios/subdominios exportando para arquivo json<br>
`python3 mywhois.py -dF dominios.txt -o result.json`

OBS: Ao exportar com a opção "-o ou -O", o formato padrão é em JSON.

Script para consultas de IP e Domínio usando APIs externas.

```
Opções:
  -h, --help            	Exibe esta ajuda. 
  -i IP, --ip IP        	Consultar um endereço IP específico, por exemplo: 192.168.1.1
  -d DOMAIN, --domain DOMAIN 	Consultar um domínio ou subdomínio específico, por exemplo: exemplo.com
  -iF IPFILE, --ipfile IPFILE	Arquivo contendo uma lista de endereços IP (um por linha). O script irá consultar cada IP listado.
  -dF DOMAINFILE		Arquivo contendo uma lista de domínios/subdomínios (um por linha). O script irá consultar cada domínio listado.
  -o OUTPUT, --output OUTPUT    Salvar os resultados das consultas em um arquivo JSON com o nome especificado.

```
