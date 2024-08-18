import pyautogui as spam # Importa a biblioteca pyautogui e atribui o alias 'spam'. Essa biblioteca permite controlar o mouse e o teclado automaticamente.
from time import sleep # Importa a função 'sleep' da biblioteca time, que pausa a execução do código por um determinado tempo.

spam.alert('O código vai começar. Aguarde o código finalizar para utilizar o computador!') # Alerta o usuário sobre o início do código e recomenda não usar o computador até o término do processo automatizado.
spam.pause = 0.5 # Define um tempo de pausa padrão de 0,5 segundo entre as ações automatizadas do pyautogui.

limite_msg = int(input('Enter n de mensagens: ')) # Solicita ao usuário o número de mensagens a serem enviadas e converte a entrada para um inteiro
user = input('Digite o nome do contato: ') # Solicita ao usuário o nome do contato ou grupo para o qual as mensagens serão enviadas.
msg = input('Coloque a mensagem: ') # Solicita ao usuário a mensagem que será enviada

spam.press('winleft') # Abre o menu Iniciar do Windows.
sleep(2) # Pausa por 2 segundos para garantir que a janela do menu Iniciar esteja aberta.
spam.write('firefox') # Digita 'firefox' para abrir o navegador Firefox.
sleep(2) # Pausa por 2 segundos antes de pressionar Enter para abrir o navegador.
spam.press('enter') # Pressiona a tecla Enter para abrir o Firefox.

sleep(10) # Pausa por 10 segundos para aguardar o carregamento do navegador.

spam.write('https://web.whatsapp.com/') # Escreve o endereço do WhatsApp Web na barra de endereços.
sleep(2) # Pausa por 2 segundos antes de pressionar Enter para acessar o site.
spam.press('enter') # Pressiona Enter para acessar o WhatsApp Web.
sleep(10) # Pausa por 10 segundos para aguardar o carregamento do WhatsApp Web.
# Move o cursor do mouse para a posição onde a barra de busca de contatos do WhatsApp Web está localizada.
spam.moveTo(200, 175, 2) # A posição X=200 e Y=175 é um exemplo; pode variar dependendo da resolução da tela e do layout do WhatsApp Web.
spam.click() # Clica na barra de busca de contatos.
spam.write(f'{user}') # Digita o nome do contato/grupo para o qual as mensagens serão enviadas.
spam.press('enter') # Pressiona Enter para abrir o chat com o contato/grupo selecionado.

sleep(5) # Pausa por 5 segundos para garantir que o chat está totalmente carregado antes de enviar as mensagens

for i in range(limite_msg): # Envia a mensagem o número de vezes especificado pelo usuário.
	spam.typewrite(msg) # Digita a mensagem 
	spam.press('Enter')	# Pressiona a tecla Enter para enviar a mensagem

print(f'{limite_msg} mensagens enviadas ao contato {user} com sucesso!') # Imprime uma mensagem de confirmação com o número de mensagens enviadas
