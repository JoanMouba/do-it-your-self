#  @uthor: Dr.-Ing. Joan MOUBA, joan.mouba@gmail.com
import string
import random

def password_generator(pwd_length: int = 8) -> str:
    """ Return a random password with at least 8 characters """
    if pwd_length < 8:
        pwd_length = 8  # at least 6 characters for strong password

    sequence_of_valid_chars = string.ascii_letters + string.digits + "!@#%_./<>"

    pwd = random.choices(sequence_of_valid_chars, k=pwd_length)
    return "".join(pwd)

if __name__ == '__main__':
    pwd_for_gmail_account = password_generator(8)
    pwd_for_linkedin_account = password_generator(12)
    pwd_for_facebook_account = password_generator(9)
    pwd_for_online_banking_account = password_generator(25)
    pwd_for_secret_account_in_switzerland = password_generator(234)  # just for fun :-)

    print(pwd_for_gmail_account)
    print(pwd_for_linkedin_account)
    print(pwd_for_facebook_account)
    print(pwd_for_online_banking_account)
    print(pwd_for_secret_account_in_switzerland)
