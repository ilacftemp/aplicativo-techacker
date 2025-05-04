import requests

def dir_search():
    dominio = input("\nDigite a URL base (ex: http://exemplo.com): ").strip()
    paths = ["admin", "login", "uploads", "images", "dashboard"]

    for path in paths:
        url = f"{dominio.rstrip('/')}/{path}"
        try:
            resposta = requests.get(url, timeout=2)
            if resposta.status_code < 400:
                print(f"[{resposta.status_code}] {url}")
        except requests.RequestException:
            pass