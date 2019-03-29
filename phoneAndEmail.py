#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re,pyperclip

phonenum_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?   # area code
(\s|-|\.)?           # separator
(\d{3})              # first 3 digits
(\s|-|\.)?           # separator
(\d{4})              # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
)''',re.VERBOSE)


email_regex = re.compile(r'''(
[a-z0-9._+%-]+          # username  
@                       # @ symbol
[a-z]+          # domain name
([a-z]{2,3}(\.[a-z]{2,3})?)    # dot-something
)''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []

phonenum_match = phonenum_regex.findall(text)
email_match = email_regex.findall(text)

for items in phonenum_match:
    matches.append(items[0])

for items in email_match:
    matches.append(items[0])
    
# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
   
