import socket

def whois_lookup():
    dominio = input("\nDigite o domínio para consulta WHOIS (no formato xxx.xxx.xxx.xxx para IP e no formato exemplo.com para domínios): ").strip()
    try:
        server = "whois.verisign-grs.com"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((server, 43))
        s.send((dominio + "\r\n").encode())
        
        resposta = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            resposta += data
        
        print(resposta.decode(errors="ignore"))
        s.close()
    except socket.timeout:
        print("Tempo limite de conexão excedido. Tente novamente mais tarde.")
    except Exception as e:
        print(f"Erro na consulta WHOIS: {e}")

whois_lookup()