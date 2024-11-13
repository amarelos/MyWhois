#-Metadata----------------------------------------------------#
#  Filename: Myshois (v1.1)              (update: 2024-11-13) #
#-Info--------------------------------------------------------#
#  Buscar por informações do alvo                             #
#-Author(s)---------------------------------------------------#
#  Amarelos ~ @amarelos                                       #
#-Licence-----------------------------------------------------#
#  MIT License ~ http://opensource.org/licenses/MIT           #
#-------------------------------------------------------------#


import argparse
import requests
import re
import os
import json

# Armazenando o TOKEN no início do script
TOKEN = os.getenv('mywhois_TOKEN')

def consultar_ip(ip):
    url = f"https://api.ip2location.io/?key={TOKEN}&ip={ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Falha na requisição: {response.status_code}"}

def consultar_dominio(domain):
    url = f"https://api.ip2whois.com/v2?key={TOKEN}&domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Falha na requisição: {response.status_code}"}

def validar_ip(ip):
    regex = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    return re.match(regex, ip) is not None

def validar_dominio(domain):
    # Regex para validar o formato do domínio
    regex = r'^(?!-)[A-Za-z0-9-]*(?<!-)(\.[A-Za-z]{2,})+$'  # Simples validação para domínios
    return re.match(regex, domain) is not None

def limpar_dominio(domain):
    return domain.split("//")[-1].split("/")[0]

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

def main():
    parser = argparse.ArgumentParser(
        description='Script para consultas de IP e Domínio usando APIs externas.'
    )
    
    parser.add_argument('-i', '--ip', type=str, 
                        help='Consultar um endereço IP específico, por exemplo: 192.168.1.1')
    parser.add_argument('-d', '--domain', type=str, 
                        help='Consultar um domínio ou subdomínio específico, por exemplo: exemplo.com')
    parser.add_argument('-iF', '--ipfile', type=str, 
                        help='Arquivo contendo uma lista de endereços IP (um por linha). O script irá consultar cada IP listado.')
    parser.add_argument('-dF', '--domainfile', type=str, 
                        help='Arquivo contendo uma lista de domínios/subdomínios (um por linha). O script irá consultar cada domínio listado.')
    parser.add_argument('-o', '--output', type=str,
                        help='Salvar os resultados das consultas em um arquivo JSON com o nome especificado.')

    args = parser.parse_args()
    
    resultados = {}

    # Consultar IP
    if args.ip:
        if validar_ip(args.ip):
            resultado_ip = consultar_ip(args.ip)
            resultados[args.ip] = resultado_ip
            print("Resultado da consulta de IP:", resultado_ip)
        else:
            print("O valor informado não corresponde a um endereço IP.")

    # Consultar arquivo de IPs
    if args.ipfile:
        ips = ler_arquivo(args.ipfile)
        for ip in ips:
            if validar_ip(ip):
                resultado_ip = consultar_ip(ip)
                resultados[ip] = resultado_ip
                print("Resultado da consulta de IP:", resultado_ip)
            else:
                print(f"Aviso: O valor '{ip}' no arquivo não corresponde a um endereço IP e será ignorado.")

    # Consultar domínio
    if args.domain:
        if validar_dominio(args.domain):
            domain_limpo = limpar_dominio(args.domain)
            resultado_dominio = consultar_dominio(domain_limpo)
            resultados[domain_limpo] = resultado_dominio
            print("Resultado da consulta de domínio:", resultado_dominio)
        else:
            print("O valor informado não corresponde a um domínio/subdomínio válido.")

    # Consultar arquivo de domínios
    if args.domainfile:
        domains = ler_arquivo(args.domainfile)
        for domain in domains:
            if validar_dominio(domain):
                domain_limpo = limpar_dominio(domain)
                resultado_dominio = consultar_dominio(domain_limpo)
                resultados[domain_limpo] = resultado_dominio
                print("Resultado da consulta de domínio:", resultado_dominio)
            else:
                print(f"Aviso: O valor '{domain}' no arquivo não corresponde a um domínio/subdomínio e será ignorado.")

    # Salvar resultados em JSON se -o for especificado
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(resultados, f, indent=4)
        print(f"Resultados salvos em {args.output}")

if __name__ == "__main__":
    main()