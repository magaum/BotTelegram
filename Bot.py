import telepot
import json
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

#carregando token do bot

load = open("token.json")
token = json.loads(load.read())
#atribuindo token ao Bot
bot = telepot.Bot(token['token'])
  
def mensagem(msg):
            tipoMsg, tipoChat, chatID = telepot.glance(msg) #Forma facilitada pela biblioteca do telepot
            if(msg['text'] == '/start'):
                    inicio(chatID, bot)
            
            elif(msg['text'] == 'Sobre os Professores'):
                    txtHelp = open('SobreProfessores\SobreOsProfessores.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
					
            elif(msg['text'] == 'Sobre Disciplinas'):
                    txtHelp = open('SobreDisciplinas\SobreDisciplinas.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
			
            elif(msg['text'] == 'Cursos'):
                    txtHelp = open('CursosOferecidos\Cursos.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
                    txtHelp.close()	#Fecha o arquivo
                        #Ler arquivos de outras pasta EX.: ComoSerAluno/Vestibular.md
			
            elif (msg['text'] == 'Como ser Aluno'):
                    txtHelp = open('ComoSerAluno\Textos\ComoSerAluno.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown', 
                    reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                    [KeyboardButton(text="Como se Inscrever"),KeyboardButton(text="Local de Provas"),
                    KeyboardButton(text="Vestibular"),KeyboardButton(text="Voltar")]	#Envia mensagem com o conteúdo do arquivo Help.txt
                    ]
                    )
                    )
                    txtHelp.close()	#Fecha o arquivo
                    #Ler arquivos de outras pasta EX.: ComoSerAluno/Vestibular.md
			
            elif(msg['text'] == 'Como se Inscrever'):
                    txtHelp = open('ComoSerAluno\Textos\ComoSeInscrever.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
                    txtHelp.close()	#Fecha o arquivo
            
            elif(msg['text'] == 'Local de Provas'):
                    txtHelp = open('ComoSerAluno\Textos\LocalDeProvas.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
                    txtHelp.close()	#Fecha o arquivo
            
            elif(msg['text'] == 'Vestibular'):
                    txtHelp = open('ComoSerAluno\Textos\Vestibular.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,txtHelp.read(),'Markdown')	#Envia mensagem com o conteúdo do arquivo Help.txt
                    txtHelp.close()	#Fecha o arquivo
                    
            elif (msg['text'] == 'Como Chegar'):
                    txtHelp = open('ComoChegar/Textos/txt01.md','r')	#Abre o arquivo Hello.md com o atributo leitura
                    bot.sendMessage(chatID,	txtHelp.read(),'Markdown',
                            reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                            [KeyboardButton(text="Fatec no Mapa"), KeyboardButton(text="Imagens"), 
                            KeyboardButton(text="Regulamento Interno"), KeyboardButton(text="Voltar")]
                            ]
                            )
                    )
    
                    txtHelp.close()	#Fecha o arquivo
					
            elif (msg['text'] == 'Horario de Aulas'):
                    txtHelp = open('RegulamentoInterno\HorarioDeAulas.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
					
            elif (msg['text'] == 'Funcionamento do EaD'):
                    txtHelp = open('RegulamentoInterno\FuncionamentoDoEaD.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
					
            elif (msg['text']== 'Faltas'):
                    txtHelp = open('RegulamentoInterno\Faltas.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
					
            elif (msg['text'] == 'Trancamento de matricula'):
                    txtHelp = open('RegulamentoInterno\TrancamentoDeMatricula.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
					
            elif(msg['text'] == 'Fatec no Mapa'):
                    bot.sendMessage(chatID,"Enviando localização...")
                    bot.sendLocation(chatID, -23.2267187,-45.9774089)

            elif (msg['text'] == 'Imagens'):
                    bot.sendMessage(chatID, "Enviando imagem...")
                    imgFatec = open("ComoChegar/Imagens/VistaFatec01.jpg","rb")
                    bot.sendPhoto(chatID, imgFatec)
                    imgFatec.close()

            elif (msg['text'] == 'Regulamento Interno'):
                    bot.sendMessage(chatID, "Enviando regulamento...")
                    doc = open ("ComoChegar/Textos/regulamentoGeral.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()
                    
            elif (msg['text'] == 'Voltar'):
                    inicio(chatID, bot)
				
def inicio(chatID, bot):
			bot.sendMessage(chatID,
            '''Olá, amigo sou o FAQtec\n
            Posso esclarecer dúvidas frequentes referente a faculdade\n
            Para escolher alguma opção selecione um botão''',
            reply_markup=ReplyKeyboardMarkup(
            keyboard=[
            [KeyboardButton(text="Como ser Aluno"), KeyboardButton(text="Cursos"),
			KeyboardButton(text="Sobre os Professores"), KeyboardButton(text="Sobre Disciplinas"),
			KeyboardButton(text="Como Chegar")]
            ]
            )
            )

			
bot.message_loop(mensagem)
#MessageLoop(bot, mensagem).run_as_thread()
while True:
            pass
