s ='JVTWBALYZJPLUJL'.lower()
counts = [0]*26
char_freq = {}
for c in s:
    char_freq[c] = char_freq.get(c, 0) + 1

p = [.08, .015, .030, .040, .130, .020, .015, .060, .065, .005, .005, .035, .030, .070, .080, .020, .002, .065, .060, .090, .030, .010, .015, .005, .020, .002]

sums = []

#get the sums for all shifts
for i in range(26):
    curr = 0
    for key, value in char_freq.items():
        curr += p[(ord(key)-ord('a')) - i] * (value/len(s))
    sums.append(curr)

for i in range(len(sums)):
    print(f'i={i}: {sums[i]}')


#max probability is shift amount
shift = sums.index(max(sums))
print(f"Best i value for shift: {shift}")

result = ""
for c in s:
    original_pos = ord(c) - ord('a')
    new_pos = (original_pos - shift) % 26
    new_char = chr(new_pos + ord('a'))
    result += new_char
print(f'Result for shift of {shift}: {result}')

