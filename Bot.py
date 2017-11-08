import telepot
import json
from ComoChegar.BtnComoChegar import BtnComoChegar
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
#carregando token do bot

load = open("token.json")
token = json.loads(load.read())

#atribuindo token ao Bot
bot = telepot.Bot("444778927:AAEIM7sIL9PM5hfl-VtqQAQaqj2-BwujQ68")

class Bot():
	def init():

		while True:	#inicia o programa e deixa em execução
			pass

	def mensagem(msg):
		updates = bot.getUpdates(-1)

		chatId = updates[0]['message']['chat']['id']	#atribuindo Id do usuário a uma variável

		try:
			username = updates[0]['message']['chat']['username']	#atribuindo nome de usuário a uma variável
		except KeyError:
			username = 'amigo'

		if(msg['text'] == "/start"):	#mandando mensagem de boas vindas ao usuário
			bot.sendMessage(	chatId,
								'''Olá, %s sou o FAQtec\n
								Posso esclarecer dúvidas frequentes referente a faculdade\n
 								Para escolher alguma opção selecione um botão''' %username,
								reply_markup=ReplyKeyboardMarkup(
    								keyboard=[
                						[KeyboardButton(text="Cursos"), KeyboardButton(text="Como ser Aluno"), KeyboardButton(text="Como Chegar")]
    								]
								)
							)

		if(msg['text'] == 'Cursos'):
			txtHelp = open('Hello.md','r')	#Abre o arquivo Hello.md com o atributo leitura
			bot.sendMessage(chatId,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
			txtHelp.close()	#Fecha o arquivo
            					#Ler arquivos de outras pasta EX.: ComoSerAluno/Vestibular.md

		elif (msg['text'] == 'Como Chegar'):
			BtnComoChegar = BtnComoChegar(bot, chatId, msg)
			BtnComoChegar.run()
			bot.sendMessage(chatId, "carlos")

	bot.message_loop(mensagem)	#Quando alguma mensagem é enviada do telegram
					            #O metodo message_loop chama a função mensagem passando o que foi enviado do telegram como parametro para função
