class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        # Encode by adding the length of the part, plus a delimiter so as to avoid errors in decoding
        for part in strs:
            encoded += str(len(part)) + "#" + part
        return encoded
    
    def decode(self, encoded: str) -> List[str]:
        decoded = []
        i = 0

        # Run through the whole string
        while i < len(encoded):
            # Use another point "j" that will find the numbers that reprent the length of a given part
            j = i
            while encoded[j] != "#":
                j += 1
            size_of_word = int(encoded[i:j])

            # After finding the size of the part, you just gotta extract it
            decoded.append(encoded[j + 1 : j + 1 + size_of_word])
            
            # Updating the pointer to get the next part
            i = j + 1 + size_of_word
        return decoded

