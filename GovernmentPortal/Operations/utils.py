import random
import string

def create_new_token(n):
    token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
    return token