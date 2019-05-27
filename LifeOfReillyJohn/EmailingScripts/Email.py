import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def Sign_Up_Confirmation(credentials, sign_up_account, username):

    with open(credentials) as file:
        gmail_user = file.readline()
        gmail_password = file.readline()

    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = sign_up_account
    msg['Subject'] = "You've Successfully Signed Up To Life Of Reilly John"
    
    
    messagePlaain = '''\t   Hey {}, You've successfully signed up to Life Of Reilly John with the email address {}\n
           Please enjoy the website and if you have any questions or issues please feel free to email this account.\n
           Thank you,
           John Reilly'''.format(username, sign_up_account)
    
    messageHTML = '''
    <h1>Welcome to Life of Reilly John</h1>
<h3>Congratulations {0}, you've successfully signed up to <a href="johnreilly.pythonanywhere.com">Life Of Reilly John</a>!</h3>
<p>You signed up with the username {0} and email address {1}.<br><br>Please feel free to email this address if you have any questions<br><br>Thank you,<br>John Reilly</p>
     '''.format(username, sign_up_account)

    msg.attach(MIMEText(messagePlaain, 'plain'))
    msg.attach(MIMEText(messageHTML, 'html'))
    text = msg.as_string()

    

    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, sign_up_account, text)
        server.quit()
        print('successfully sent the mail')
    except Exception as e:
        server.quit()
        print(e)
        print("failed to send mail")
    

