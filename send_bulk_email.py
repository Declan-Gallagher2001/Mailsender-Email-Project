from mailersend import MailerSendClient, EmailBuilder
import pandas as pd

# Set your API key here - Need from Admin
mailer = MailerSendClient(api_key="")

# Read the Excel file (no headers, first column is name, second column is email)
df = pd.read_excel('recipients.xlsx', header=None, names=['name', 'email'])

# Sender information - Need info 
mail_from = {
    "name": "",
    "email": "",
}

# Template ID now updated to use OUSBA
template_id = "neqvygmevzw40p7w"

# Subject
subject = "Email Test"

# Loop through each recipient and send email
for index, row in df.iterrows():
    recipient_name = row['name']
    recipient_email = row['email']

    # Skip if email is empty or invalid
    if pd.isna(recipient_email) or recipient_email == '':
        print(f"Skipping row {index + 1}: No email address")
        continue

    # Build the email
    email = EmailBuilder()
    email.from_email(mail_from["email"], mail_from["name"])
    email.to(recipient_email, recipient_name)
    email.subject(subject)
    email.template(template_id)
    email.personalize(recipient_email, name=recipient_name)

    # Send the email
    try:
        response = mailer.emails.send(email.build())
        print(f"✓ Email sent to {recipient_name} ({recipient_email})")
    except Exception as e:
        print(f"✗ Failed to send email to {recipient_name} ({recipient_email}): {str(e)}")

print("\n✓ All emails processed!")
