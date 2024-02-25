base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# 1. For our first problem, write a function that converts a given base-62 string
#    into an integer. Only a single string will be provided, and it will be up to
#    11 characters in length.

def to_base_10(videoId):

    # Begin by reversing videoId
    videoId = videoId[::-1]

    # Define int to sum all values into base10:
    total = 0

    # With videoId reversed, the index value should now correspond to the
    # base power value (i.e. first letter now represents 62^0 value, second is 62^1 value, and so on)
    for i, letter in enumerate(videoId):

        # Calculate the base10 value of the letter at current index/power,
        # and add it to the total sum:
        total += (62 ** i) * base_62.find(letter)

    # After for loop exits, the total should be the base10 value:
    return total

# 2. Write a function that does the opposite of the previous one. 
# That is, it encodes a base 10 number into base 62
# producing a string that represents the same number.

def to_base_62(number):

    # Define str for the converted base62 value:
    final_char = ""

    while number > 0:

        # Take the modulo of number, which should give us the remainder.
        # The remainder represents the base10 equivalent of "rightmost" power value for base62.
        current = number % 62
        # Get the base62 equivalent for the base10 value we found above:
        current_char = base_62[current]

        # Put the current_char at the beginning of the final_char. As while loop continues, this will
        # place the character at correct position.
        final_char = current_char + final_char
        # Perform floor division, which will give the "base62 right shifted" value.
        number = number // 62

        # We will do this until number reaches zero!

    return final_char
