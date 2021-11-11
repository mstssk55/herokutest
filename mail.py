import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64
from email.mime.text import MIMEText
from apiclient import errors
# 1. Gmail APIのスコープを設定
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
# 2. メール本文の作成
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    encode_message = base64.urlsafe_b64encode(message.as_bytes())
    return {'raw': encode_message.decode()}
# 3. メール送信の実行
def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
# 4. メインとなる処理
# 5. アクセストークンの取得
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'js/credentials.json', SCOPES)
        creds = flow.run_local_server()
    with open('token.json', 'w') as token:
            token.write(creds.to_json())
service = build('gmail', 'v1', credentials=creds)
# 6. メール本文の作成
sender = ''
to = 'mstssk55@gmail.com'
subject = 'メール送信自動化テスト'
message_text = 'メール送信の自動化テストをしています。'
message = create_message(sender, to, subject, message_text)
# 7. Gmail APIを呼び出してメール送信
send_message(service, 'me', message)