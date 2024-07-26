def find_complement(num):
    
    bit_length = num.bit_length()
    
    bitmask = (1 << bit_length) - 1
    
    return num ^ bitmask

# Test cases
print(find_complement(5))   
print(find_complement(1))   