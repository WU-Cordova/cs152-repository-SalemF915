import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._number_of_buckets = number_of_buckets
        self._load_factor = load_factor
        self._custom_hash_function = custom_hash_function


        self._buckets = [[] for _ in range(self._number_of_buckets)]  # Create a list of empty lists
        self._size = 0  # Keep track of how many key-value pairs are in the map


    def __getitem__(self, key: KT) -> VT:

        # Step 1: Compute the hash
        if self._custom_hash_function:
            hash_value = self._custom_hash_function(key)
        else:
            hash_value = hash(key)
        bucket_index = hash_value % self._number_of_buckets

        # Step 2: Get the correct bucket
        bucket = self._buckets[bucket_index]

        # Step 3: Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v  # Key found, return the value

        # Step 4: Key not found, raise an error
        raise KeyError(f"Key {key} not found in HashMap.")



    def __setitem__(self, key: KT, value: VT) -> None:  

        # Step 1: Compute the hash
        if self._custom_hash_function:
            hash_value = self._custom_hash_function(key)
        else:
            hash_value = hash(key)
        


        bucket_index = hash_value % self._number_of_buckets

        # Step 2: Get the right bucket
        bucket = self._buckets[bucket_index]

        # Step 3: Search for the key in the bucket
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        # Step 4: Key not found, insert new key-value pair
        bucket.append((key, value))
        self._size += 1


    def keys(self) -> Iterator[KT]:
        raise
    
    def values(self) -> Iterator[VT]:
        raise NotImplementedError("HashMap.values() is not implemented yet.")

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        # Step 1: Compute the hash
        if self._custom_hash_function:
            hash_value = self._custom_hash_function(key)
        else:
            hash_value = hash(key)
        
        bucket_index = hash_value % self._number_of_buckets

        #Gets the correct bucket 
        bucket = self._buckets[bucket_index]

        
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                # Step 4: Key found, remove the key-value pair
                del bucket[idx]
                self._size -= 1
                return


        # Step 5: Key not found, raise an error
        raise KeyError(f"Key {key} not found in HashMap.")

    
    def __contains__(self, key: KT) -> bool:
        if self._custom_hash_function:
            hash_value = self._custom_hash_function(key)
        else:
            hash_value = hash(key)
        
        bucket_index = hash_value % self._number_of_buckets

        #Gets the correct bucket 
        bucket = self._buckets[bucket_index]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                # Step 4: Key found, remove the key-value pair
                return True
        
        return False

    
    def __len__(self) -> int:
        return self._size
    
    def __iter__(self) -> Iterator[KT]:
        for buck in self._buckets:      # Step 1: go through each bucket
            for (k, v) in buck:    # Step 2: go through each key-value pair
                yield k
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)