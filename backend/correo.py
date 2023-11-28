import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviarCorreoElectronicoGes(email, link):
    # Configurar los detalles del correo electrónico
    remitente = "cmdf@alpix.cl"
    destinatario = email
    asunto = "Formulario GES"
    mensaje = f"<html><body><p>Hola, aquí tienes el enlace al formulario GES: <a href='{link}'>{link}</a></p></body></html>"

    # Crear el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Agregar el cuerpo del mensaje en formato HTML
    msg.attach(MIMEText(mensaje, 'html'))

    # Enviar el correo electrónico
    try:
        #server = smtplib.SMTP('mail.alpix.cl', 465)
        server = smtplib.SMTP('mail.alpix.cl', 587)
        #server.starttls()
        server.login(remitente, "6en;A@r~AkW&")
        server.send_message(msg)
        server.quit()
        print("Correo electrónico enviado correctamente")
    except Exception as e:
        print("Error al enviar el correo electrónico:", str(e))