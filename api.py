import requests

class Cody:
    def __init__(self):
        self.base_url = "https://getcody.ai/api/v1"
        self.conversation_id = "CONVERSATION ID"
        self.api_key = "API KEY"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get_response(self, message):
        url = self.base_url + '/messages'
        data = {
            'content': message,
            'conversation_id': self.conversation_id
        }

        response = requests.post(url, headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json()['data']['content']
        
        else:
            return 'Something went wrong'
    