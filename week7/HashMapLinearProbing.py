from hashFuncs import hashFunc, hash2Index

# Instead of creating an entirely new class for each element of the HashMap (like I did with Chaining method),
# I will just use python's tuple class to store key value pair. Assume first item in tuple is key, and second
# item is the value.


class HashMapLinearProbing:

    def __init__(self, table_len=10):

        # Initialize a table with length 10:
        self.table_len = table_len
        self.table = [None for i in range(table_len)]

        # Keep track of how many nodes (elements) are in the table:
        self.node_count = 0
    
    def getValue(self, key):
        table_index = hash2Index(hashFunc(key), self.tableLen)
        
        # Get the element at table_index:
        ele = self.table[table_index]

        # If there's nothing there, that means the key doesn't exist within the HashMap. Raise KeyError:
        if not ele:
            raise KeyError(key)
        
        # Otherwise, we need to begin linear probing until we find an element that matches our key.
        # Initialize a variable that represents how far we will travel from the original table_index
        # before finding the matching key.
        delta = 0

        while delta < self.tableLen:

            # If we found the matching key, return its value:
            if ele[0] == key:
                return ele[1]
            
            # Otherwise, we increment delta and seek out the next index to check.
            delta += 1
            # We need to grab new element at table_index + delta. If delta exceeds the length of the
            # table, we can use modulo operator to bring it back to the 0 index:
            new_index = (table_index + delta) % self.tableLen
            # Re-define element:
            ele = self.table[new_index]
        
        # If the above while loop exited, it means the key does not exist within the hash map. Raise KeyError:
        raise KeyError(key)




