import random
import smtplib

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(receiver_email, otp):
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

    message = f'Subject: OTP Verification\n\nYour OTP: {otp}'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

def verify_otp(receiver_email, otp):
    if otp == entered_otp:
        print('OTP Successfully Validated!')
    else:
        print('OTP verification failed.')
otp = generate_otp()
entered_otp = None
receiver_email = input('Enter your email address: ')
send_email(receiver_email, otp)
print('OTP sent to your email.')
entered_otp = input('Enter the OTP: ')
verify_otp(receiver_email, otp)
