import smtplib

sender_enviar = "correodepruebas12025@gmail.com"
receiver_recibe = ("mariaisaac181013@gmail.com", 
                   "orlandoisaac181013.ossp23452@gmail.com", 
                   "orlandosalas99@gmail.com")

password_contraseña = "vpiu snqy bvew m.........wer"
subject_asunto = "Hola"
body_cuerpomensaje = "This is Python, aprendiendo como enviar correos desde codigo."

message_mensaje = f"""\
From: {sender_enviar},
To:  {receiver_recibe},
Subject: {subject_asunto}\n
{body_cuerpomensaje}"""

servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls()

try: 
    servidor.login(sender_enviar, password_contraseña)
    print("Login exitoso")
    servidor.sendmail(sender_enviar, receiver_recibe, message_mensaje)
    print("Correo enviado con exito")
except smtplib.SMTPAuthenticationError:
    print("Error de autenticacion: Verifica tu usuario y contraseña")