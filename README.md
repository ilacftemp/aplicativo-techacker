# Documentação Técnica

**Descrição:** Aplicativo em linha de comando (CLI) voltado para reconhecimento em testes de intrusão, com integração de múltiplas ferramentas simples.

## Estrutura do projeto:

```
aplicativo-techacker/
  - main.py
  - scanner.py
  - dnslookup.py
  - subdomain_enum.py
  - whois_lookup.py
  - dirsearch.py
  - requirements.txt
  - README.md
  - .gitignore
```

**Dependências:** Bibliotecas: `scapy`, `requests`, `socket`, `ipaddress`, `re`

## Instalação:

```bash
pip install -r requirements.txt
```

## Descrição dos módulos:

- **Portscan:** Escaneia um host ou rede, definindo portas e protocolo (TCP/UDP). Detecta serviços e sistema operacional via banner.
- **DNS Lookup:** Devolve o IP associado a um domínio inserido.
- **Enumeração de Subdomínios:** Testa subdomínios comuns de um domínio base.
- **WHOIS Lookup:** Retorna dados públicos do registro de um domínio.
- **Busca por diretórios:** Verifica se diretórios como `/admin`, `/login`, etc., estão acessíveis em uma URL.
- **Sair:** Encerra o aplicativo.

## Execução:

```bash
python main.py
```

# Manual do Usuário

Ao iniciar o programa, o usuário verá o seguinte menu:

```
Bem-vindo ao ReconApp!
1. Portscan
2. DNS Lookup
3. Enumeração de Subdomínios
4. WHOIS Lookup
5. Busca por diretórios
6. Sair
Escolha uma opção:
```

Cada módulo executado descreve o tipo de input que deve receber.