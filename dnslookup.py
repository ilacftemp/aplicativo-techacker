import socket

def dns_lookup():
    dominio = input("\nDigite o domínio para resolver (ex: exemplo.com): ").strip()
    try:
        ip = socket.gethostbyname(dominio)
        print(f"Endereço IP de {dominio}: {ip}")
    except socket.gaierror:
        print("Erro: domínio inválido ou inacessível.")