def truncated(num, num1):
    sn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
    163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
     227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
      281, 283, 293]
    
    for i in sn:
        while num%i== 0 and num1%i == 0:
            num = num/i
            num1 = num1 / i
    return f'{int(num)}/{int(num1)}'

def devision(num1,num2):
    whole = num1//num2
    numerator = num1%num2
    fraction = truncated(numerator, num2)
    if whole == 0:
        return fraction
    else:
        if num1%num2 == 0:
            return int(whole)
        else:
            return f'{whole} {fraction}'

#a = input()
#b = input()
#print(devision(float(a),float(b)))
