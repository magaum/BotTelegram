from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import telepot
#bot = telepot.Bot("444778927:AAEIM7sIL9PM5hfl-VtqQAQaqj2-BwujQ68")


class BtnComoChegar():

	def __init__(self, bot, chatId, msg):
		self.bot = bot
		self.chatId = chatId
		self.msg = msg

	def run(self):
		while True:
			pass

		txtHelp = open('ComoChegar/Textos/txt01.md','r')	#Abre o arquivo Hello.md com o atributo leitura

		self.bot.sendMessage(	self.chatId,
								txtHelp.read(),'Markdown',
								reply_markup=ReplyKeyboardMarkup(
									keyboard=[
										[KeyboardButton(text="Fatec no Mapa"), KeyboardButton(text="Imagens"), KeyboardButton(text="Regulamento Interno")]
									]
								)
							)

		txtHelp.close()	#Fecha o arquivo

		if(self.msg['text'] == 'Fatec no mapa'):
			self.bot.sendMessage(chatId,"teste - fatec no mapa")
			self.bot.sendLocation(chatId, -23.2267187,-45.9774089)

		elif (self.msg['text'] == 'Imagens'):
			self.bot.sendMessage(self.chatId,"teste - Imagens")
			imgFatec = open("ComoChegar/Imagens/VistaFatec01.jpg","rb")
			self.bot.sendPhoto(self.chatId, imgFatec)
			imgFatec.close()

		elif (self.msg['text'] == 'Regulamento Interno'):
			self.bot.sendMessage(self.chatId,"teste - Regulamento Interno")
			doc = open ("ComoChegar/Textos/regulamentoGeral.pdf",'rb')
			self.bot.sendDocument(self.chatId, doc)
			doc.close()

#	bot.message_loop(run)
