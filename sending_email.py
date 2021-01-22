import smtplib #secure mail transfer protocol
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls() #transport layer security

#Next, log in to the server
server.login("ksaichaitanya73960@gamil.com", "7095945318")

#Send the mail
msg = "Hello! first mail using python script THANK YOU SIR" # The /n separates the message from the headers
server.sendmail("ksaichaitanya73960@gmail.com", "sakethreddy.kallepu@gmail.com", msg) 
