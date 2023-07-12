from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

# Parâmetros
senha = "dourados"
remetente = "danielteste383@gmail.com"
destinatario = "kevenrodriguesotto@gmail.com"
assunto = "E-mail com Python"

# Configuração do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

try:
    # Criação do servidor
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    # Login na conta para envio
    server.login(remetente, senha)

    # Envio da mensagem
    server.sendmail(remetente, destinatario, msg.as_string())

    print('Mensagem enviada com sucesso')
except Exception as e:
    print(f"Ocorreu um erro ao enviar a mensagem: {e}")

finally:
    # Encerramento do servidor
    server.quit()

