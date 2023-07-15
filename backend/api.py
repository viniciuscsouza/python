import urllib3              
import json      
import certifi


http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

def pesquisar_endereco(cep):
    """
    Busca informações de endereço usando um serviço web de consulta de CEP.

    Parâmetros:
    cep (str): O CEP a ser pesquisado.

    Retorna:
    dict: Um dicionário contendo as informações de endereço associadas ao CEP.
          As chaves do dicionário são os seguintes campos:
          - cep: O CEP pesquisado.
          - logradouro: O nome do logradouro (rua, avenida etc.).
          - complemento: Informações adicionais do endereço.
          - bairro: O bairro da localidade.
          - localidade: A cidade ou município.
          - uf: A sigla do estado.
          - ibge: O código IBGE da cidade.
          - gia: O código GIA da cidade.
          - ddd: O código DDD da região.
          - siafi: O código SIAFI da cidade.

    Exemplo de uso:
    >>> endereco = pesquisar_endereco("12345-678")
    >>> print(endereco['logradouro'])
    "Rua Exemplo"
    >>> print(endereco['localidade'])
    "São Paulo"
    """
    resp = http.request("GET", f"https://viacep.com.br/ws/{cep}/json/")
    decodificar_resp = resp.data.decode('utf-8')
    dicionario = json.loads(decodificar_resp)
    return dicionario   

def pesquisar_cep(uf, cidade, logradouro):
    """
    Pesquisa um CEP com base na UF (Unidade Federativa), cidade e logradouro fornecidos.
    
    Parâmetros:
    - uf (str): Sigla da Unidade Federativa (exemplo: 'SP' para São Paulo)
    - cidade (str): Nome da cidade
    - logradouro (str): Nome do logradouro (rua, avenida, etc.)
    
    Retorna:
    - dicionario (dict): Dicionário contendo as informações do CEP encontrado
    
    Exemplo de uso:
    >>> resultado = pesquisar_cep('SP', 'São Paulo', 'Avenida Paulista')
    >>> print(resultado)
    {'cep': '01311-300', 'logradouro': 'Avenida Paulista', 'complemento': 'de 1047/1048 ao fim', 
     'bairro': 'Bela Vista', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 
     'ddd': '11', 'siafi': '7107'}
    """
    resp = http.request("GET", f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/")
    decodificar_resp = resp.data.decode('utf-8')
    dicionario = json.loads(decodificar_resp)
    return dicionario



def soma(numero_a, numero_b):
    return numero_a + numero_b