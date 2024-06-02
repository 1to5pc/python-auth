import hashlib

SUPPORTED_HASHES = hashlib.algorithms_available 

class Hasher():
    def __init__(self, hash_name: str, initial_data: bytes = b'', **kwargs):
        if not (hash_name in SUPPORTED_HASHES):
            raise ValueError(f"{hash_name} is not a supported hashing algorithm")
        self.__hash_implementation: hashlib._Hash = hashlib.new(hash_name, initial_data, **kwargs)
        self.__kwargs = kwargs
    
    # Convenient but wont show up in lsp, might have to define each method later
    def __getattr__(self, name):
        return getattr(self.__hash_implementation, name)
    
    def hexdigest(self, shake_output_size: int=None) -> bytes:
        if self.__hash_implementation.name in ('shake_128', 'shake_256'):
            if shake_output_size:
                return self.__hash_implementation.hexdigest(shake_output_size)
            # Good default output sizes for shake
            elif self.__hash_implementation.name == 'shake_128':
                return self.__hash_implementation.hexdigest(32)
            elif self.__hash_implementation.name == 'shake_256':
                return self.__hash_implementation.hexdigest(64)
        return self.__hash_implementation.hexdigest()
    
    def clear_hasher(self) -> None:
        self.__hash_implementation = hashlib.new(self.__hash_implementation.name, b'', **self.__kwargs)
