import random
import time

def obter_nome_jogador():
    nome = input("Digite seu nome: ").strip()
    return nome

def obter_escolha_jogador():
    while True:
        escolha = input("Escolha Pedra, Papel ou Tesoura: ").strip().lower()
        if escolha in ['pedra', 'papel', 'tesoura']:
            return escolha
        else:
            print("Escolha inválida! Tente novamente.")

def obter_escolha_maquina():
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha = random.choice(opcoes)
    return escolha

def determinar_vencedor(jogador, maquina):
    if jogador == maquina:
        return "empate"
    elif (jogador == 'pedra' and maquina == 'tesoura') or \
         (jogador == 'tesoura' and maquina == 'papel') or \
         (jogador == 'papel' and maquina == 'pedra'):
        return "jogador"
    else:
        return "maquina"

def jo_ken_po():
    contagem = ["Jo", "Ken", "Po!"]
    for palavra in contagem:
        print(palavra)
        time.sleep(1)  # Pausa de 1 segundo entre as palavras

def jogar():
    nome = obter_nome_jogador()
    pontos_jogador = 0
    pontos_maquina = 0
    
    while True:
        jogador = obter_escolha_jogador()
        maquina = obter_escolha_maquina()
        
        print(f"{nome}, você escolheu: {jogador}")
        time.sleep(1)  # Adiciona uma pausa de 1 segundo
        jo_ken_po()
        print(f"A máquina escolheu: {maquina}")
        
        vencedor = determinar_vencedor(jogador, maquina)
        
        if vencedor == "jogador":
            print("Você venceu!")
            pontos_jogador += 1
        elif vencedor == "maquina":
            print("Você perdeu!")
            pontos_maquina += 1
        else:
            print("Empate!")
        
        print(f"Placar: {nome} {pontos_jogador} x {pontos_maquina} Máquina")
        
        continuar = input("Deseja jogar novamente? (digite 'sair' para parar): ").strip().lower()
        if continuar == 'sair':
            print(f"Obrigado por jogar, {nome}! Placar final: {nome} {pontos_jogador} x {pontos_maquina} Máquina")
            break
        else:
            continue

jogar()
