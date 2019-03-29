#! python3
#simple python program to save password for different sites

import sys,pyperclip

#this dictionary save the site name and password 
my_passwords = {'twitter':'326737gfdj%yy','facebook':'gdfwyyuwetgye536','github':'UIIOiueuh7847hf&*j','stackoverflow':'ioOIJo**&Jfj89j', 'codewars':'gjdfi!)E46^7DFRT'}


if len(sys.argv) < 2:
    print ('Usage: python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]

if account in my_passwords:
    pyperclip.copy(my_passwords[account])
    print ('password for '+account+' copied to clipboard.')
else:
    print ('There is no account named '+account)
