# MailerSend Bulk Email Project

This project allows you to send bulk personalized emails using MailerSend and data from an Excel file.

## Files Included

- **send_bulk_email.py** - Main script to send emails to all recipients in Excel file
- **mailersend_example.py** - Example script to send a single test email
- **recipients.xlsx** - Excel file with recipients (Column 1: Name, Column 2: Email)

## Setup Instructions

### 1. Install Python 3
Make sure Python 3 is installed on your system.

### 2. Create Virtual Environment
```bash
cd "C:\Users\D.Gallagher\Documents\MailerSend Bulk Email Project"
python3 -m venv venv
```

### 3. Activate Virtual Environment
**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Required Packages
```bash
pip install mailersend pandas openpyxl
```

## How to Use

### Send Bulk Emails
1. Update `recipients.xlsx` with your recipient data (Column 1: Name, Column 2: Email)
2. Make sure your virtual environment is activated
3. Run:
```bash
python send_bulk_email.py
```

### Send Single Test Email
```bash
python mailersend_example.py
```

## Configuration

### API Key
Current API key: ``

### Template ID
Current template: `pr9084zy8r8gw63d`

### Sender Email
From: Declan Gallagher <declangallagher@gallaghertech.co.uk>

### Subject Line
"Hello from Gallagher Tech"

## Notes

- Make sure your sender domain is verified in MailerSend
- Trial accounts can only send to administrator email addresses
- The Excel file should have NO headers (just data starting from row 1)
- Each email is personalized with the recipient's name from the Excel file

## Troubleshooting

**Error: Domain not verified**
- Go to MailerSend dashboard → Domains
- Verify your domain by adding DNS records

**Error: Trial account restrictions**
- Trial accounts can only send to the admin email
- Upgrade your MailerSend account or use admin email for testing

**Error: Module not found**
- Make sure virtual environment is activated
- Reinstall packages: `pip install mailersend pandas openpyxl`

## Support

For issues with MailerSend, visit: https://www.mailersend.com/help
