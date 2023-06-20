print('''
Your email will be splitted into username, domain and extension''')
email = input('Enter your email: ')

def email_validity(n):
    if '@' in n:
        email_splitter(n)
    # else:
    #     print('Invalid email')

def email_splitter(n):
    (username,domain) = n.split('@')
    (domain,extension) = domain.split('.')
    print(f'Username: {username}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension}')

while True:
    email_validity(email)
