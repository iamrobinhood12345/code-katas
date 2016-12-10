# code-katas

What Century
- Module: what_century.py
- Tests: test_what_century.py
- Link: https://www.codewars.com/kata/what-century-is-it/
```
def whatCentury(year):
    indicators = {'1': 'st', '2': 'nd', '3': 'rd'}
    century = str(int(year) // 100 + (1 if int(year) % 100 > 0 else 0))
    return century + (indicators.get(century[-1], 'th') if century[0] != '1' else 'th')
```
For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
- Module: ufc.py
- Tests: test_ufc.py
- Link: https://www.codewars.com/kata/for-ufc-fans-total-beginners-conor-mcgregor-vs-george-saint-pierre/
```
statements = {
    'george saint pierre': "I am not impressed by your performance.",
    'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"
}

def quote(fighter):
    return statements[fighter.lower()]
```
Convert a string to an array
- Module: convert_string.py
- Tests: test_convert_string.py
- Link: https://www.codewars.com/kata/convert-a-string-to-an-array/
```
def string_to_array(string):
    return string.split(" ")

Sum of the first nth term of Series
- Module: sum_nth_series.py
- Tests: test_sum_nth_series.py
- Link: http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
```
Fake Binary
- Module: fake_binary.py
- Tests: test_fake_binary.py
- Link: https://www.codewars.com/kata/fake-binary/python
```
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
```
Remove First and Last Character
- Module: remove_first_last.py
- Tests: test_remove_first_last.py
- Link: https://www.codewars.com/kata/remove-first-and-last-character/
```
def remove_char(s):
    return s[1 : -1]
```
Find the Position
- Module: find_the_position.py
- Tests: test_find_the_position.py
- Link: https://www.codewars.com/kata/find-the-position/
```
def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)
```
Where My Anagrams At
- Module: anagrams.py
- Tests: test_anagrams.py
- Link: https://www.codewars.com/kata/where-my-anagrams-at/python
```
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
```
Human Readable Time
- Module: human_time.py
- Tests: test_human_time.py
- Link: https://www.codewars.com/kata/human-readable-time/python
```
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
```
