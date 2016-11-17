"""
    @author shrikant aher
"""
import socket
import re
import smtplib


def check_syntax(email):
    """
        check email using regex and return true if valid
        :param email: string of email for validation
        return True if valid else return None
    """
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
        email)
    if match is None:
        return None
    return True


def check_email(email):
    """
        check the email is valid or not using google server
        :param email: mail id for validation
        :return Success if valid else Return Bad
    """
    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect('ALT1.ASPMX.L.GOOGLE.COM')
    server.helo(host)
    server.mail(email)
    code, message = server.rcpt(str(email))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        return 'Success'
    else:
        return 'Bad'

if __name__ == "__main__":
    print "enter mail id"
    email_id = raw_input()
    if check_syntax(email_id):
        print check_email(email_id)
