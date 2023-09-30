import os

def processar_resposta(resposta):
    if resposta == '1':
        print(f'{os.linesep}Botija de 13kg Custa: R$115 no dinheiro ou pix.{os.linesep}Caso seja no cartão custa R$120')
    elif resposta == '2':
        print(f'{os.linesep}Botija de 7kg Custa: R$75 no dinheiro ou pix.{os.linesep}Caso seja no cartão custa R$80')
    elif resposta == '3':
        print(f'{os.linesep}Agua Crim Custa: R$10 no dinheiro ou pix.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}Agua Nova agua: R$8.00 no dinheiro ou pix.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}Agua Toya: R$8.00 no dinheiro ou pix.{os.linesep}')
    elif resposta == '6':
        print(f'{os.linesep}Aguarde um instante que ja iremos lhe atender.{os.linesep}:')
    else:
        print('Digite apenas 1,2,3,4,5,6')
    
def start():
    while True:
        print('Olá! Bem vindo a Distribuidora El-shaday. Localizada no Coroado III.')
        print('Qual seria o seu pedido hoje?')
    
        resposta = input(
          f'[1] - Botija de 13kg(Grande){os.linesep}[2] - Botija de 7kg(Pequena){os.linesep}[3] - Agua Crim{os.linesep}[4] - Agua Nova agua{os.linesep}[5] - Agua Toya{os.linesep}[6] - Falar com revendedor')
 
        processar_resposta(resposta)
        
        endereço = input('Qual seu endereço:')

        forma_de_pagamento = input(f'Qual a forma de pagamento?{os.linesep}[1]-PIX,{os.linesep}[2]-DINHEIRO,{os.linesep}[3]-CARTÃO{os.linesep}:')

        if forma_de_pagamento == '3':
            print('Ok. Estamos enviando a entrega com a maquininha.')
            break

        elif forma_de_pagamento == '1':
            print("92991744839 Nome:Rosangela Franca Leite")
            break

        elif forma_de_pagamento == '2':    
            troco = input('Precisa de troco? [1] - Sim  [2] - Não.')  
        if troco == '1':
            troco_necessario = input('Quanto precisa de troco?')
        elif troco =='2':
            print('Anotado.')

        print('Obrigado pela preferencia. Volte sempre!!')

        break

if __name__ == '__main__':
    start()