# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado


def verificar_status_aluno(nota1, nota2, nota3):
    
    media = (nota1 + nota2 + nota3) / 3
    

    if media >= 7:
        return f"Nota: {media:.2f} - Aprovado"
    elif 5 <= media < 7:
        return f"Nota: {media:.2f} - Recuperação"
    else:
        return f"Nota: {media:.2f} - Reprovado"


def main():
    
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")
        return
    
    
    resultado = verificar_status_aluno(nota1, nota2, nota3)
    print(resultado)


if __name__ == "__main__":
    main()

