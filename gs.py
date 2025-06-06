"""
Projeto: Apoio Climático
Descrição: Sistema que auxilia na visualização de alertas climáticos, informações do clima atual e estatísticas regionais,
e permite preencher um formulário de apoio em situações de emergência climática.
Autores: Enzo Amá - RM: 562138
         Leonardo Borges - RM: 565966
         Paulo Henrique - RM: 562179
"""

import random

# Funções auxiliares
def menu_principal():
    """Exibe o menu principal com as opções disponíveis."""
    print("\nBem-vindo ao Apoio Climático, o que você deseja:")
    print("1 - Verificar alertas na sua região")
    print("2 - Ver clima atual da sua cidade")
    print("3 - Ver estatísticas da região")
    print("4 - Preencher formulário de apoio")
    print("5 - Sair")

def alerta_regional():
    """Exibe alertas climáticos para a região informada."""
    regiao = input("\nDigite sua região (norte, sul, sudeste, centro-oeste, nordeste): ").lower()
    
    if regiao not in ["norte", "sul", "sudeste", "centro-oeste", "nordeste"]:
        print("Região inválida. Tente novamente.")
        return

    tem_alertas = random.choice([True, False])
    print(f"\nAlertas para a região {regiao.title()}")
    if tem_alertas:
        alertas = [
            "Alerta de chuvas intensas nas próximas 24h.",
            "Risco de alagamento em áreas urbanas.",
            "Aviso de cheia em rios da região.",
            "Deslizamentos possíveis em encostas íngremes."
        ]
        qtd = random.randint(1, len(alertas))
        escolhidos = random.sample(alertas, k=qtd)
        for i, alerta in enumerate(escolhidos, 1):
            print(f"{i}. {alerta}")
    else:
        print("Nenhum alerta registrado para esta região no momento.")

def clima_atual():
    """Exibe informações do clima atual para a cidade informada."""
    cidade = input("\nDigite o nome da sua cidade para verificar o clima: ")
    temperatura = random.randint(15, 40)
    umidade = random.randint(20, 100)
    pluviosidade = random.randint(0, 50)

    print(f"\nClima Atual em {cidade.title()}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
    print(f"Pluviosidade: {pluviosidade} mm")

    if pluviosidade > 40:
        print("Risco de enchente alto! Planeje uma rota de fuga caso necessário.")
    elif pluviosidade > 20:
        print("Risco de enchente moderado, fique atento aos possíveis alertas.")
    else:
        print("Risco baixo de enchente até o momento.")

def estatisticas_regiao():
    """Exibe estatísticas climáticas da região informada."""
    regiao = input("\nDigite sua região (norte, sul, sudeste, centro-oeste, nordeste): ").lower()
    
    if regiao not in ["norte", "sul", "sudeste", "centro-oeste", "nordeste"]:
        print("Região inválida. Tente novamente.")
        return

    total_alertas = random.randint(0, 20)
    media_pluviosidade = round(random.uniform(5, 40), 2)
    locais_risco = ["área ribeirinha", "centro urbano", "zona industrial", "área montanhosa", "região costeira"]
    selecionados = random.sample(locais_risco, 3)

    print(f"\nEstatísticas da Região {regiao.title()}")
    print(f"Total de alertas no mês: {total_alertas}")
    print(f"Média de pluviosidade: {media_pluviosidade} mm")
    print(f"Locais com maior risco de impacto climático: {', '.join(selecionados)}")
    print("Esses dados auxiliam no planejamento de ações emergenciais.")

def formulario_apoio():
    """Coleta informações do usuário para solicitar apoio em situações emergenciais."""
    print("\nFormulário de Apoio")
    nome = input("Nome completo: ")
    cidade = input("Cidade: ")
    necessidade = input("Descreva sua necessidade ou situação: ")

    print(f"\nObrigado, {nome}!")
    print("Sua solicitação foi registrada. Equipes de apoio serão informadas.")

# Execução principal
def executar():
    """Loop principal que gerencia as opções do menu."""
    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            alerta_regional()
        elif escolha == "2":
            clima_atual()
        elif escolha == "3":
            estatisticas_regiao()
        elif escolha == "4":
            formulario_apoio()
        elif escolha == "5":
            print("Saindo do sistema. Mantenha-se seguro!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do sistema
if __name__ == "__main__":
    executar()
