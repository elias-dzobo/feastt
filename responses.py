import hashlib


h = hashlib.new('sha256')

name = b'@12345hex'

h.update(name)

hashed_name = h.hexdigest()

print(hashed_name)

def test():
    assert hashlib.sha256(b'@12345hex').hexdigest() == hashed_name


print(test())