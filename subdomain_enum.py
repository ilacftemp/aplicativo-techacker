import socket

def subdomain_enum():
    dominio = input("\nDigite o domínio base (ex: exemplo.com): ").strip()
    subdominios = ["www", "mail", "ftp", "test", "dev", "api"]

    for sub in subdominios:
        subdominio = f"{sub}.{dominio}"
        try:
            ip = socket.gethostbyname(subdominio)
            print(f"{subdominio} -> {ip}")
        except socket.gaierror:
            pass