import re

def email_parse(email):
    RE_EMAIL = re.compile(r"([\w]+)@(\w+\.\w{2,})")
    RE_EMAIL.match(email), f'wrong email {email}'
    if RE_EMAIL.match(email) is None:
        raise ValueError(f'wrong email:  {email}')
    match = re.search(RE_EMAIL, email)
    my_dict = {'username': match[1], 'domain': match[2]}
    print(my_dict)


email_parse('someone@geekbrains.ru')
email_parse('som123eone@geekbrains.ru')
email_parse('someone123@geekbrainsru')
