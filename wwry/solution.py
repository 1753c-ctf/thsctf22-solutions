from hashlib import md5, sha256

i=0
with open("Q:\\rockyou\\rockyou2.txt",'r', encoding='latin-1') as infile:
    for line in infile:
        hash = sha256(('THSCTF{'+line.strip()+'}').encode('utf-8')).hexdigest()
        if(hash == '2d9df8f29342675ab4d1d7265d12eb5e0cfa86d1fb6e5e8d56cce429cad2f292'):
            text1 = 'THSCTF{'+line.strip()+'}'
            print(f'{text1}')
        
print("done")
