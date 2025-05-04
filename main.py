from scanner import scanner
from dnslookup import dns_lookup
from subdomain_enum import subdomain_enum
from whois_lookup import whois_lookup
from dirsearch import dir_search

def main():
    while True:
        print("\nBem-vindo ao ReconApp!")
        print("1. Portscan")
        print("2. DNS Lookup")
        print("3. Enumeração de Subdomínios")
        print("4. WHOIS Lookup")
        print("5. Busca por diretórios")
        print("6. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            scanner()
        elif escolha == "2":
            dns_lookup()
        elif escolha == "3":
            subdomain_enum()
        elif escolha == "4":
            whois_lookup()
        elif escolha == "5":
            dir_search()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()