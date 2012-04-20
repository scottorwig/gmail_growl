import ConfigParser
import imaplib
import subprocess

config = ConfigParser.ConfigParser()
config.read('settings.cfg')

user = config.get('account', 'user')
phrase = config.get('account', 'pass')
growlnotify_path = config.get('growl', 'path')

obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
obj.login(user,phrase)
obj.select()
print obj
#if len(obj.search(None, 'UnSeen')[1][0].split()) > 0:
if config.get('growl','notified') == 'no':
    print "You've got mail!"
    config.set('growl','notified','yes')

growlnotify_args = [growlnotify_path, 'pythondata']
print 'growlnotify args are {0}'.format(growlnotify_args)
p = subprocess.Popen(growlnotify_args)
