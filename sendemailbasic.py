import smtplib

# Specifying the from and to addresses

fromaddr = 'news.janela@gmail.com'
toaddrs  = 'ankurchauhan21@gmail.com, news.janela@gmail.com'

# Writing the message (this message will appear in the email)

msg = 'Welcome Janela'

# Gmail Login

username = 'news.janela'
password = 'windowcuba'

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
