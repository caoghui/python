

def bin2int():
    B = '1101'
    I = 0
    while B != '':
        I = I * 2 + (ord(B[0]) - ord('0'))
        B = B[1:] 


print(bin2int())
