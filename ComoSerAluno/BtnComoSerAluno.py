class ComoSerAluno():
	
	def __init__(self, bot):
		self.bot = bot
		txtHelp = open('Hello02.md','r')	#Abre o arquivo Hello.md com o atributo leitura
		bot.sendMessage(chatId,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
		txtHelp.close()	#Fecha o arquivo
	                    #Ler arquivos de outras pasta EX.: ComoSerAluno/Vestibular.md
