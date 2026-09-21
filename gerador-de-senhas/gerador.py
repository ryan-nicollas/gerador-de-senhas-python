import random
import string


def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    return senha


def verificar_forca(tamanho, numeros, simbolos):
    if tamanho >= 12 and numeros and simbolos:
        return "Forte"
    elif tamanho >= 8:
        return "Média"
    else:
        return "Fraca"


print("=" * 35)
print("       🔐 GERADOR DE SENHAS")
print("=" * 35)

while True:

    try:
        tamanho = int(input("\nTamanho da senha: "))

        if tamanho < 4:
            print("❌ A senha deve ter pelo menos 4 caracteres.")
            continue

    except ValueError:
        print("❌ Digite um número válido.")
        continue

    maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == "s"
    numeros = input("Incluir números? (s/n): ").lower() == "s"
    simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

    senha = gerar_senha(
        tamanho,
        maiusculas,
        numeros,
        simbolos
    )

    forca = verificar_forca(tamanho, numeros, simbolos)

    print("\n" + "=" * 35)
    print(f"🔑 Senha gerada: {senha}")
    print(f"🛡️ Força da senha: {forca}")
    print("=" * 35)

    novamente = input("\nDeseja gerar outra senha? (s/n): ").lower()

    if novamente != "s":
        print("\nPrograma encerrado. 👋")
        break