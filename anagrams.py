def anagrams(word, words):
    def is_anagram(test, orig):
        a=''.join(sorted(test))
        b=''.join(sorted(orig))
        if a==b:
            return True
        else:
            return False
    return_me=[]
    for i in range(0,len(words)):
        if is_anagram(words[i],word):
            return_me.append(words[i])
    return return_me    