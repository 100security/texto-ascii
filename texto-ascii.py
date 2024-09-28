# 100SECURITY
# Converter Textos e Arquivos <> ASCII
# Por: Marcos Henrique
# Site: www.100security.com.br

import binascii
import os
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')
        
clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
projeto = f"{Style.BRIGHT}{Fore.YELLOW}# - - - - - - - - 100SECURITY - - - - - - - - #\n"
titulo = f"{Style.BRIGHT}{Fore.GREEN}Converter Textos e Arquivos <> ASCII"
github = f"{Style.BRIGHT}{Fore.WHITE}GitHub: {Fore.WHITE}github.com/100security/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto-ascii"
instagram = f"{Style.BRIGHT}{Fore.WHITE}Instagram: {Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}@100security"

# Exibe o texto com as cores e com uma nova linha entre eles
print(f"{projeto}\n{titulo}\n{github}\n{instagram}")

# Função para converter texto em ASCII
def text_to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values

# Função para converter ASCII para texto
def ascii_to_text(ascii_values):
    text = ''.join([chr(value) for value in ascii_values])
    return text

# Função para converter arquivo de texto em ASCII
def text_file_to_ascii(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        ascii_values = text_to_ascii(text)
        return ascii_values
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter ASCII de arquivo para texto
def ascii_file_to_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            ascii_values = list(map(int, file.read().split()))
        return ascii_to_text(ascii_values)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão. Verifique o conteúdo do arquivo.")

# Função para converter arquivos binários em ASCII (hexadecimal)
def file_to_ascii(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        ascii_representation = binascii.hexlify(binary_data).decode('utf-8')
        return ascii_representation
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter ASCII de um arquivo (hexadecimal) para arquivo binário
def ascii_file_to_binary(input_file, output_file):
    try:
        # Ler o conteúdo ASCII (representação em hexadecimal) do arquivo
        with open(input_file, 'r', encoding='utf-8') as file:
            ascii_data = file.read().strip()  # Remover espaços em branco extras

        # Converter o conteúdo hexadecimal de volta para binário
        binary_data = binascii.unhexlify(ascii_data)
        
        # Escrever os dados binários no arquivo de saída
        with open(output_file, 'wb') as file:
            file.write(binary_data)
        
        print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Arquivo {output_file} criado com sucesso!")
    except binascii.Error:
        print(f"{Style.BRIGHT}{Fore.RED}Erro ao converter ASCII para binário. Verifique o conteúdo do arquivo {input_file}.")
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo {input_file} não encontrado.")

# Função para salvar o conteúdo em um arquivo
def salvar_em_arquivo(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Resultado salvo em {file_name}")

# Função para exibir o menu
def exibir_menu():
    print(f"\n{Style.BRIGHT}{Fore.RED}# - - - - - - - - - M E N U - - - - - - - - - #\n")
    print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}ASCII")
    print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}ASCII {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto.txt {Fore.WHITE}para {Fore.LIGHTYELLOW_EX}ASCII")
    print(f"{Style.BRIGHT}{Fore.WHITE}4 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}ascii.txt {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}5 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Arquivos {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}ASCII")
    print(f"{Style.BRIGHT}{Fore.WHITE}6 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}ASCII {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Arquivo")
    print(f"{Style.BRIGHT}{Fore.WHITE}7 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTRED_EX}Sair\n")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            texto = input("Digite o Texto a ser convertido para ASCII: ")
            ascii_result = text_to_ascii(texto)
            ascii_str = ' '.join(map(str, ascii_result))
            salvar_em_arquivo('ascii.txt', ascii_str)
            print(f"Texto original: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto}")
            print(f"Conversão para ASCII: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{ascii_str}")
        
        elif opcao == '2':
            ascii_input = input("Digite os valores ASCII separados por espaço: ")
            try:
                ascii_values = list(map(int, ascii_input.split()))
                texto_result = ascii_to_text(ascii_values)
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Valores ASCII: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{ascii_values}")
                print(f"Conversão para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}Entrada inválida. Por favor, insira apenas números inteiros separados por espaços.")
        
        elif opcao == '3':
            file_path = input("Digite o nome do arquivo de texto (.txt): ")
            ascii_result = text_file_to_ascii(file_path)
            if ascii_result:
                ascii_str = ' '.join(map(str, ascii_result))
                salvar_em_arquivo('ascii.txt', ascii_str)
                print(f"Conversão de {file_path} para ASCII: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{ascii_str}")
        
        elif opcao == '4':
            file_path = input("Digite o nome do arquivo de ASCII (.txt): ")
            texto_result = ascii_file_to_text(file_path)
            if texto_result:
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Conversão de {file_path} para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '5':
            file_path = input("Digite o nome do arquivo (ex: imagem.png, arquivo.pdf): ")
            ascii_result = file_to_ascii(file_path)
            if ascii_result:
                salvar_em_arquivo('ascii.txt', ascii_result)
                print(f"Conversão de {file_path} para ASCII: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{ascii_result}")
        
        elif opcao == '6':
            input_file = input("Digite o nome do arquivo ASCII (ex: ascii.txt): ")
            output_file = input("Digite o nome do arquivo de saída (ex: imagem.png, arquivo.pdf): ")
            ascii_file_to_binary(input_file, output_file)

        elif opcao == '7':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()