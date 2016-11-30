#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        count = 0

        for bucket in self.buckets:
            # bucket should be a list containing the key value pairs
            count += bucket.length()

        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        
        for bucket in self.buckets:
            current = bucket.head

            while current.next is not None:
                if current.data == key:
                    return True
                current = current.next
            # for node in bucket:
            #     if node.data == key:
            #         return True

        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        for bucket in self.buckets:
            data = bucket.find(lambda _key: _key == key)
            if data is not None:
                return data[1]
            # current = bucket.head

            # while current.next is not None:
            #     if current.data[0] == key:
            #         return current.data[1]
            #     current = current.next

        raise ValueError

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        hashKey = hash(key) % len(self.buckets)
        bucket = self.buckets[hashKey]
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        for bucket in self.buckets:
            value = bucket.get(key)
            # ^ or self.get(key)?
            bucket.delete((key, value))
            # current = bucket.head

            # while current.next is not None:
            #     if current.data[0] == key:
            #         #remove key val pair from hash table
            #     current = current.next

        raise ValueError

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets
        pass

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        pass
