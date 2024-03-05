from hashHelpers import hashFunc, hash2Index


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
        table_index = hash2Index(hashFunc(key), self.table_len)

        # Get the element at table_index:
        ele = self.table[table_index]

        # If there's nothing there, that means the key doesn't exist within the HashMap. Raise KeyError:
        if not ele:
            raise KeyError(key)

        # Otherwise, we need to begin linear probing until we find an element that matches our key.
        # Initialize a variable that represents how far we will travel from the original table_index
        # before finding the matching key.
        delta = 0

        while delta < self.table_len:

            # If we found the matching key, return its value:
            if ele and ele[0] == key:
                return ele[1]

            # Otherwise, we increment delta and seek out the next index to check.
            delta += 1
            # We need to grab new element at table_index + delta. If delta exceeds the length of the
            # table, we can use modulo operator to bring it back to the 0 index:
            new_index = (table_index + delta) % self.table_len
            # Re-define element:
            ele = self.table[new_index]

        # If the above while loop exited, it means the key does not exist within the hash map. Raise KeyError:
        raise KeyError(key)

    def setValue(self, key, value):

        table_index = hash2Index(hashFunc(key), self.table_len)
        # Get the element at table_index:
        ele = self.table[table_index]

        # Initialize a variable to keep track of where you are in the hash table:
        delta = 0

        while delta < self.table_len:

            # If current index is unoccupied (i.e. null element at current index), add the
            # input key and value here, and increment node_count. Rehash if threshold load
            # factor exceeds 0.75:
            if not ele:
                self.table[table_index] = (key, value)
                self.node_count += 1

                if self.node_count / self.table_len > 0.75:
                    self._rehash()

                # Exit out of the function:
                return None

            # If a key/value tuple already exists in current index, check if that tuple has the same key
            # as the input. Update the value if this is the case:
            if ele[0] == key:
                self.table[table_index] = (key, value)
                return None

            # Otherwise, increment delta and seek out the next index to check.
            delta += 1
            table_index = (table_index + delta) % self.table_len
            # Re-define element:
            ele = self.table[table_index]

        # If the above while loop exits somehow (rehash function should trigger before that happens)
        # raise IndexError notifying the user that table is full
        raise IndexError("Hash table is completely full!")

    def _rehash(self):

        # Initialize a temporary stack to store all the nodes within current table.
        temp = []

        # Loop through current HashMap's table, and append each tuple to temp:
        for i in range(self.table_len):

            # If there is a valid tuple, append to temporary stack:
            if self.table[i]:
                temp.append(self.table[i])

        # Increase the table size, and add all the items back to the larger HashMap table.
        # Increase by size 10:
        self.table_len += 10
        self.table = [None for i in range(self.table_len)]

        # Reset node_count:
        self.node_count = 0
        # Remove all the items 1 by 1 from temp stack, and add them to our newly sized table:
        while temp:
            current_key, current_val = temp.pop()
            self.setValue(current_key, current_val)

        # Rehash complete!
        return None
