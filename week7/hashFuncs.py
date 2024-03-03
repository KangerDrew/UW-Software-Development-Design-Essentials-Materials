# For my hash function, I will assume the input is a base62 value, and
# convert it to base10 value. This is better hashing method than what was
# covered in class, as switching the placement of the letter will result in
# different hash value [ex. "ab" => 2269, "ba" => 2330]

# I will be re-using my submission from the first assignemnt as a hash function:
def hashFunc(input_str):

    base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    input_str = input_str[::-1]
    total = 0

    for i, letter in enumerate(input_str):

        b_62_val = base_62.find(letter)

        # If user attempts to use a str that's not part of base62,
        # raise error, letting them know to use base62 value:
        if b_62_val == -1:
            raise IndexError("Please use valid base62 value for your key!")
        
        total += (62 ** i) * b_62_val

    return total

# Provide the hash value, and the size of the array to get its index:
def hash2Index(hashValue, size):
    return hashValue % size


print(5/3)
