from mailersend import MailerSendClient, EmailBuilder

# Set your API key here
mailer = MailerSendClient(api_key="mlsn.ea6931199ab1ea93c6472c95454ba5eb28874fbf58a65d05b5ef739feceb8af1")

# Build the email
email = EmailBuilder()
email.from_email("declangallagher@gallaghertech.co.uk", "Declan Gallagher")
email.to("declanmagill00@gmail.com", "Declan Magill")
email.subject("Hello from Gallagher Tech")
email.template("pr9084zy8r8gw63d")
email.personalize("declanmagill00@gmail.com", name="Declan Magill")

# Send the email
response = mailer.emails.send(email.build())
print(f"Email sent! Response: {response}")
