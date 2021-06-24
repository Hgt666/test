class Login:
    def __init__(self,session):
        self.session=session
    def doLogin(self):
        self.url_login="http://api.k780.com"
        self.data_login={
            'app': 'weather.realtime',
            'weaid': '2',
            'ag': 'today',
            'sign': 'SIGN',
            'format': 'json',
        }
        self.resp=self.session.post(self.url_login,self.data_login)
        print(self.resp)