import ConfigParser
import imaplib

config = ConfigParser.ConfigParser()
config.read('settings.cfg')

user = config.get('account', 'user')
phrase = config.get('account', 'pass')

obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
obj.login(user,phrase)
obj.select()
#obj.search(None,'UnSeen')
print obj
if len(obj.search(None, 'UnSeen')[1][0].split()) > 0:
    print "You've got mail!"
