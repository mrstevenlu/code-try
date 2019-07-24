import rsa

key = rsa.newkeys(2222)
public_key = key[0]
private_key = key[1]

pub = public_key.save_pkcs1()
pubfile = open('public.pem', 'wb')
pubfile.write(pub)
pubfile.close()

pri = private_key.save_pkcs1()
prifile = open('private.pem', 'wb')
prifile.write(pri)
prifile.close()

with open('public.pem')as publicfile:
    p=publicfile.read()
    public_key=rsa.PublicKey.load_pkcs1(p)

msg='message for testing.......'
byte_msg=msg.encode()
crypted_msg=rsa.encrypt(byte_msg,public_key)
print('-------debug:crypted_msg is [%s]'%crypted_msg)

with open('private.pem')as privatefile:
    p=privatefile.read()
    private_key=rsa.PrivateKey.load_pkcs1(p)

byte_msg=rsa.decrypt(crypted_msg,private_key)
msg=byte_msg.decode()
print('originalk message is[%s]'%msg)
