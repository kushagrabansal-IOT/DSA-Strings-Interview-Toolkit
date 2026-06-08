# Tests — DSA-Strings-Interview-Toolkit
# Run: pytest tests/ -v

def test_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ["a","c"]

def test_kmp():
    assert kmp_search("AABAACAADAABAABA","AABA") == [0,9,12]
    assert kmp_search("AAAA","AA") == [0,1,2]
    assert kmp_search("ABC","D") == []

def test_group_anagrams():
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    assert len(result) == 3

def test_min_window():
    assert min_window("ADOBECODEBANC","ABC") == "BANC"
    assert min_window("a","a") == "a"
    assert min_window("a","b") == ""

def test_longest_unique():
    assert longest_unique("abcabcbb") == 3
    assert longest_unique("bbbbb") == 1
    assert longest_unique("pwwkew") == 3