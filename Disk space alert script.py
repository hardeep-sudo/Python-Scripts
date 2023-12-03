import subprocess
import mandrill

threshold = 95
partition = "/"

def send_mandrill_email(html_text, to_email, from_email, from_name, subject, tags):
    '''send email through mandrill'''
    mandrill_client = mandrill.Mandrill('add you key here')
    message = {
        'from_email': from_email,
        'from_name': from_name,
        'headers': {'Reply-To': from_email},
        'html': html_text,
        'important': True,
        'preserve_recipients': None,
        'subject': subject,
        'tags': tags,
        'to': [{'email': to_email,
             'type': 'to'}],
        'track_clicks': True,
        'track_opens': True}

    result = mandrill_client.messages.send(message=message)

def check_once():
 df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
 for line in df.stdout:
     splitline = line.decode().split()
     try:
         if int(splitline[4][:-1]) > threshold:
             print(splitline)
             send_mandrill_email("mysql threshold exceeded 95%", "to.email@example.com", "from.email@example.com", "Name", "CRITICAL: MYsql disc space exceeded", ["mysql"])
             break
     except:
         continue
check_once()