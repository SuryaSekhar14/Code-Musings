s = "Surya Sekhar Datta"
charFreq = {}

s = s.lower()
s.replace(" ", "")

for ch in s:
    if ch in charFreq:
        charFreq[ch] += 1
    else:
        charFreq[ch] = 1


keys = list(charFreq.keys())

print(sorted(keys))