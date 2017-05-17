# code-katas

        platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
        rootdir: /Users/ben/401/code-katas/code-katas, inifile: 
        plugins: cov-2.4.0
        collected 48 items 

        src/test_anagrams.py ......
        src/test_convert_string.py .....
        src/test_fake_binary.py .....
        src/test_find_the_position.py ...
        src/test_remove_first_last.py .....
        src/test_sum_nth_series.py .............
        src/test_ufc.py ....
        src/test_what_century.py .......

        ---------- coverage: platform darwin, python 2.7.13-final-0 ----------
        Name                            Stmts   Miss  Cover   Missing
        -------------------------------------------------------------
        src/anagrams.py                    12      0   100%
        src/convert_string.py               2      0   100%
        src/fake_binary.py                  7      0   100%
        src/find_the_position.py            2      0   100%
        src/human_time.py                  15     15     0%   1-18
        src/remove_first_last.py            3      0   100%
        src/sum_nth_series.py               5      0   100%
        src/test_anagrams.py                7      0   100%
        src/test_convert_string.py          5      0   100%
        src/test_fake_binary.py             5      0   100%
        src/test_find_the_position.py       5      0   100%
        src/test_human_time.py              0      0   100%
        src/test_remove_first_last.py       5      0   100%
        src/test_sum_nth_series.py          5      0   100%
        src/test_ufc.py                     5      0   100%
        src/test_what_century.py            5      0   100%
        src/ufc.py                          9      0   100%
        src/what_century.py                16      2    88%   11, 17
        -------------------------------------------------------------
        TOTAL                             113     17    85%


        ========================== 48 passed in 0.21 seconds ===========================

-

        platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
        rootdir: /Users/ben/401/code-katas/code-katas, inifile: 
        plugins: cov-2.4.0
        collected 48 items 

        src/test_anagrams.py ......
        src/test_convert_string.py .....
        src/test_fake_binary.py .....
        src/test_find_the_position.py ...
        src/test_remove_first_last.py .....
        src/test_sum_nth_series.py .............
        src/test_ufc.py ....
        src/test_what_century.py .......

        ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
        Name                            Stmts   Miss  Cover   Missing
        -------------------------------------------------------------
        src/anagrams.py                    12      0   100%
        src/convert_string.py               2      0   100%
        src/fake_binary.py                  7      0   100%
        src/find_the_position.py            2      0   100%
        src/human_time.py                  15     15     0%   1-18
        src/remove_first_last.py            3      0   100%
        src/sum_nth_series.py               5      0   100%
        src/test_anagrams.py                7      0   100%
        src/test_convert_string.py          5      0   100%
        src/test_fake_binary.py             5      0   100%
        src/test_find_the_position.py       5      0   100%
        src/test_human_time.py              0      0   100%
        src/test_remove_first_last.py       5      0   100%
        src/test_sum_nth_series.py          5      0   100%
        src/test_ufc.py                     5      0   100%
        src/test_what_century.py            5      0   100%
        src/ufc.py                          9      0   100%
        src/what_century.py                16      2    88%   11, 17
        -------------------------------------------------------------
        TOTAL                             113     17    85%


        ========================== 48 passed in 0.24 seconds ===========================


What Century: 6th Kyu
- Module: what_century.py
- Tests: test_what_century.py
- Link: https://www.codewars.com/kata/what-century-is-it/
```
def whatCentury(year):
    indicators = {'1': 'st', '2': 'nd', '3': 'rd'}
    century = str(int(year) // 100 + (1 if int(year) % 100 > 0 else 0))
    return century + (indicators.get(century[-1], 'th') if century[0] != '1' else 'th')
```
For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre: 8th Kyu
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
Convert a string to an array: 8th Kyu
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
Fake Binary: 8th Kyu
- Module: fake_binary.py
- Tests: test_fake_binary.py
- Link: https://www.codewars.com/kata/fake-binary/python
```
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
```
Remove First and Last Character: 8th Kyu
- Module: remove_first_last.py
- Tests: test_remove_first_last.py
- Link: https://www.codewars.com/kata/remove-first-and-last-character/
```
def remove_char(s):
    return s[1 : -1]
```
Find the Position: 8th Kyu
- Module: find_the_position.py
- Tests: test_find_the_position.py
- Link: https://www.codewars.com/kata/find-the-position/
```
def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)
```
Where My Anagrams At: 5th Kyu
- Module: anagrams.py
- Tests: test_anagrams.py
- Link: https://www.codewars.com/kata/where-my-anagrams-at/python
```
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
```
Human Readable Time: 5th Kyu
- Module: human_time.py
- Tests: test_human_time.py
- Link: https://www.codewars.com/kata/human-readable-time/python
```
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
```
