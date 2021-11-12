# Shifts and Mask operations

# --------------------------------------------------------------------------------------------------
# Logical Shifts
# 2**x, x>0: shifts <==  multiplying
# 2**x, x<0: shifts ==> dividing

# Arithmetic Shifts
# multiplying and dividing but for Two's Complement 
# retains leading 1s when shifting a negative binary number

# Masking
# AND - used to turn off bits: input(10011010) + mask(11100110) = output(10000010)
# OR - used to turn on bits: input(10011010) + mask(11100110) = output(1111110)

# --------------------------------------------------------------------------------------------------
# Utility Functions

def zero_packing(binary, length):
    '''
    Packs binary string with zeros until a given length
        e.g. zero_packing('11001', 8)
    returns '00011001' which is in byte form
    '''

    binary = binary[::-1] # reverses binary strinf so it can be more easily packed with leading zeros
    if len(binary) % length:
        zeros = length - len(binary)
        binary += '0' * zeros  # packs necessary amount of leading zeros into string
    return binary[::-1] # returns binary

# --------------------------------------------------------------------------------------------------
# Shifting

def logical_shift_mul(binary ,shift_num):
    binary = bin(int(binary, 2) << shift_num)
    binary = zero_packing(binary[2:], 8)
    return binary[abs(len(binary) - 8):]

def logical_shift_div(binary ,shift_num):
    binary = bin(int(binary, 2) >> shift_num)
    binary = zero_packing(binary[2:], 8)
    return binary[abs(len(binary) - 8):]

def arithmetic_shift_mul(binary, shift_num):
    sign = binary[0]
    binary = bin(int(binary, 2) << shift_num)
    binary = zero_packing(binary[2:], 8)
    binary = binary[abs(len(binary) - 8):]
    binary = sign + binary[1:]
    return binary

