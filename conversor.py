print("Bem vindo ao conversor.")
escolha = int(input("Digite 1 para converter quilômetros em milhas e 2 para converter milhas em quilômetros."))

if escolha == 1:
    print("Você escolheu converter quilômetros para milhas.")
    kms = float(input("Digite quantos quilômetros deseja converter em milhas: "))
    converter = 0.621371
    milhas = kms * converter
    print(f"{kms} quilômetros são iguais a {round(milhas)} milhas.")
elif escolha == 2:
    print("Você escolheu converter milhas para quilômetros.")
    milhas = float(input("Digite quantas milhas deseja converter em quilômetros: "))
    converter = 1.60934
    kms = milhas * converter
    print(f"{milhas} milhas são iguais a {round(kms)} quilômetros.")