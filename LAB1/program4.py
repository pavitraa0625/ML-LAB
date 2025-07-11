text = "hippopotamus"
text = text.lower()

freq = {}

for ch in text:
    if ch.isalpha():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

max_char = max(freq, key=freq.get)
print("Max character is:", max_char)
print("Count is:", freq[max_char])
