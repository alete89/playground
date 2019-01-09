from Crypto.PublicKey import ECC

a = ECC.generate(curve="P-256")
print(a)

f = open("myprivkey.pem", "wt")
f.write(a.export_key(format="PEM"))
f.close()

o = open("myprivkey.pem", "rt")
key = ECC.import_key(o.read())
print(key)
