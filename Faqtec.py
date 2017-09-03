import telepot

#atribuindo token ao Bot
bot = telepot.Bot("444778927:AAEIM7sIL9PM5hfl-VtqQAQaqj2-BwujQ68")

#cria um loop infinito
while(True):
#atribuindo ultimas atualizações feitas por usuários ("mensagens encaminhadas para o bot")
  count = 0
  updates = bot.getUpdates(-1)
#atribuindo Id do usuário a uma variável
  chatId = updates[0]['message']['chat']['id']
#atribuindo nome de usuário a uma variável
  username = updates[0]['message']['chat']['username']
  mensagem = updates[0]['message']['text']
#mandando mensagem de boas vindas ao usuário
  if(mensagem == "/start"):
    bot.sendMessage(chatId, 'biiirl %s'%username)
