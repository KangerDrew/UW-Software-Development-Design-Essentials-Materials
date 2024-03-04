from hashHelpers import hashFunc, hash2Index


# The HashNode in this case will be a linked list node:
class HashNodeC:

    def __init__(self, key, value, node=None):
        self.key = key
        self.value = value
        self.next = node


class HashMapChaining:

    def __init__(self, table_len=10):

        # Initialize a table with length 10:
        self.table_len = table_len
        self.table = [None for i in range(table_len)]

        # Keep track of how many nodes (elements) are in the table:
        self.node_count = 0

    def getValue(self, key):
        table_index = hash2Index(hashFunc(key), self.table_len)

        # Get the "head node" of the linked list at table_index:
        head = self.table[table_index]
        # If there's nothing there, that means the key doesn't exist within the HashMap. Raise KeyError:
        if not head:
            raise KeyError(key)

        # Otherwise, we need to check through the linked list:
        while head:

            # If we find the match, return its value:
            if head.key == key:
                return head.value

            # Increment pointer to next node:
            head = head.next

        # Raise KeyError if the key wasn't found within the linked list:
        raise KeyError(key)

    def setValue(self, key, value):

        table_index = hash2Index(hashFunc(key), self.table_len)
        # Get the "head node" of the linked list at table_index:
        head = self.table[table_index]
        # If there's nothing there, create the new node, and increment node_count by 1:
        if not head:
            self.table[table_index] = HashNodeC(key, value)
            self.node_count += 1

            # New Node has been added. Check if rehash is necessary (i.e. threshold load factor exceeds 1.5):
            if self.node_count / self.table_len > 1.5:
                self._rehash()

            return None

        # Otherwise, we need to check through the linked list. This time, we'll need the
        # reference to the previous node also:
        prev = None
        while head:
            # If we happen to run into a node with identical key, we replace its value:
            if head.key == key:
                head.value = value
                # No need to increment node_count.
                return None

            # Increment the prev and head pointers:
            prev = head
            head = head.next

        # If the above while loop exited without returning, it means that the key did not
        # exist within the linked list. So create a new one at the end (prev pointer should
        # be at the end of the linked list)

        prev.next = HashNodeC(key, value)
        self.node_count += 1

        # New Node has been added. Check if rehash is necessary:
        if self.node_count / self.table_len > 1.5:
            self._rehash()

        return None

    def _rehash(self):

        # Initialize a temporary stack to store all the nodes within current table.
        # In other statically typed language (ex. Java, C#, etc.), we need to specify
        # the size of this temporary storage. If such were the case, I'd set the size
        # to be equal to the table_len * 1.5. But Python doesn't care lol:
        temp = []

        # Loop through current HashMap's table, and append each node to temp:
        for i in range(self.table_len):

            current = self.table[i]

            while current:
                # There's a valid HashNode, so append its key and value to temporary storage:
                temp.append((current.key, current.value))
                # Increment current pointer:
                current = current.next

        # At this point, all the key & value pairs from original table should be
        # in the temporary storage. Increase the table size, and add all the items
        # back to the larger HashMap table.

        # Begin by resetting the node_count:
        self.node_count = 0

        # Increase by size 10:
        self.table_len += 10

        # Reset table:
        self.table = [None for i in range(self.table_len)]

        # Remove all the items 1 by 1 from temp stack, and add them to our newly sized table:
        while temp:
            current_key, current_val = temp.pop()
            self.setValue(current_key, current_val)

        # Rehash complete!
        return None
