phones=['iphone', 'samsung', 'xiaomi']
phones_add=['honor','samsung']
phones.extend(phones_add)
print(phones)
print(len(phones))
print(phones.count('samsung'))
phones.remove('samsung')
print(phones.count('samsung'))
print(phones[:3])
print(phones.index('honor'))