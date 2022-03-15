import smtplib, ssl

sender_email = "ore.oomisore@gmail.com"
receiver_email = "ooomisor@uwaterloo.ca"
message = """\
subject: hi there

This message is sent from Python."""


# Starting a Secure SMTP Connection
port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("ore.oomisore@gmail.com", password)

    # Sending Plain-text Email
    server.sendmail(sender_email, receiver_email, message)
