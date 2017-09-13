import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

#atribuindo token ao Bot
bot = telepot.Bot("444778927:AAEIM7sIL9PM5hfl-VtqQAQaqj2-BwujQ68")

class Bot():
  def init():
#inicia o programa e deixa em execução
    while True:
      pass
     
  def mensagem(msg):
    #atribuindo ultimas atualizações feitas por usuários ("mensagens encaminhadas para o bot")
      updates = bot.getUpdates(-1)
    #atribuindo Id do usuário a uma variável
      chatId = updates[0]['message']['chat']['id']
    #atribuindo nome de usuário a uma variável
      username = updates[0]['message']['chat']['username']
    #mandando mensagem de boas vindas ao usuário
      if(msg['text'] == "/start"):
        bot.sendMessage(chatId,'''Olá, %s sou o FAQtec\n     
 Posso esclarecer dúvidas frequentes referente a faculdade\n
 Para escolher alguma opção selecione um botão''' %username,
      reply_markup=ReplyKeyboardMarkup(
          keyboard=[
            [KeyboardButton (text="Como ser aluno"),KeyboardButton (text="Cursos"),KeyboardButton (text="Professores")]
                   ]
      ))

      if(msg['text'] == 'Cursos'):
#Abre o arquivo Hello.md com o atributo leitura
        txtHelp = open('Hello.md','r')
  
  #Ler arquivos de outras pasta EX.: ComoSerAluno/Vestibular.md
  
#Envia mensagem com o conteúdo do arquivo Help.txt
        bot.sendMessage(chatId,txtHelp.read(),'Markdown')
#Fecha o arquivo
        txtHelp.close()

#Quando alguma mensagem é enviada do telegram
#O metodo message_loop chama a função mensagem passando o que foi enviado do telegram como parametro para função        
  bot.message_loop(mensagem)