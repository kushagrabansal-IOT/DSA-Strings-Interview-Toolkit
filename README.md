# DSA-Strings-Interview-Toolkit 📝

[![Python](https://img.shields.io/badge/Language-Python_3.11-3776ab?style=flat&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat)](LICENSE)
[![DSA](https://img.shields.io/badge/Category-DSA-f97316?style=flat)](#)
[![Stars](https://img.shields.io/github/stars/kushagrabansal-IOT/DSA-Strings-Interview-Toolkit?style=social)](https://github.com/kushagrabansal-IOT/DSA-Strings-Interview-Toolkit)
[![Interview Ready](https://img.shields.io/badge/Interview-Ready-7c3aed?style=flat)](#)

> Complete string algorithm toolkit — palindromes, anagrams, KMP pattern matching, Rabin-Karp, Z-algorithm, suffix arrays. 40+ interview problems with solutions.

**Built by [Kushagra Bansal](https://github.com/kushagrabansal-IOT) | Founder @ Project Lab India, Jaipur**

---

## 📌 Topics Covered

| # | Topic | Key Problems |
|---|-------|-------------|
| 1 | String Manipulation | Reverse, Rotate, Compress |
| 2 | Palindrome Problems | Longest palindromic substring, DP |
| 3 | Anagram Detection | Group anagrams, Valid anagram |
| 4 | KMP Algorithm | O(n+m) pattern matching |
| 5 | Rabin-Karp | Rolling hash pattern search |
| 6 | Z-Algorithm | Z-array, pattern occurrences |
| 7 | Sliding Window on Strings | Longest unique, Min window |

---

## 📋 Problem Statements

### Problem 1 — Longest Palindromic Substring
> Find the longest substring that reads the same forwards and backwards.
> `Input: "babad"` → `Output: "bab"` or `"aba"`

### Problem 2 — KMP Pattern Matching
> Find all occurrences of pattern in text in O(n+m) time.
> `Input: text="AABAACAADAABAABA", pattern="AABA"` → `Output: [0, 9, 12]`

### Problem 3 — Group Anagrams
> Group strings that are anagrams of each other.
> `Input: ["eat","tea","tan","ate","nat","bat"]` → `Output: [["bat"],["nat","tan"],["ate","eat","tea"]]`

### Problem 4 — Minimum Window Substring
> Find smallest substring containing all chars of target.
> `Input: s="ADOBECODEBANC", t="ABC"` → `Output: "BANC"`

### Problem 5 — Longest Substring Without Repeating Characters
> `Input: "abcabcbb"` → `Output: 3` ("abc")

---

## 💻 Solutions + Time & Space Complexity

```python
# DSA-Strings-Interview-Toolkit — Core Solutions
# Author: Kushagra Bansal — Project Lab India

def longest_palindrome(s):
    """Expand Around Center — Manacher-inspired
    Time: O(n²) | Space: O(1)
    """
    res = ""
    for i in range(len(s)):
        for odd, even in [(i,i),(i,i+1)]:
            l,r = odd, even
            while l>=0 and r<len(s) and s[l]==s[r]: l-=1; r+=1
            if r-l-1 > len(res): res = s[l+1:r]
    return res

def kmp_search(text, pattern):
    """KMP pattern matching with LPS array
    Time: O(n+m) | Space: O(m)
    """
    def build_lps(p):
        lps=[0]*len(p); j=0
        for i in range(1,len(p)):
            while j>0 and p[i]!=p[j]: j=lps[j-1]
            if p[i]==p[j]: j+=1
            lps[i]=j
        return lps
    lps=build_lps(pattern); j=0; matches=[]
    for i,c in enumerate(text):
        while j>0 and c!=pattern[j]: j=lps[j-1]
        if c==pattern[j]: j+=1
        if j==len(pattern): matches.append(i-j+1); j=lps[j-1]
    return matches

def group_anagrams(strs):
    """Group anagrams using sorted string as key
    Time: O(n·k log k) | Space: O(n·k)
    """
    from collections import defaultdict
    d = defaultdict(list)
    for s in strs: d[tuple(sorted(s))].append(s)
    return list(d.values())

def min_window(s, t):
    """Minimum window substring — Sliding Window
    Time: O(n) | Space: O(1) [bounded alphabet]
    """
    from collections import Counter
    need=Counter(t); have={}; formed=0; req=len(need)
    l=0; best=(float('inf'),0,0)
    for r,c in enumerate(s):
        have[c]=have.get(c,0)+1
        if c in need and have[c]==need[c]: formed+=1
        while formed==req:
            if r-l+1 < best[0]: best=(r-l+1,l,r)
            lc=s[l]; have[lc]-=1
            if lc in need and have[lc]<need[lc]: formed-=1
            l+=1
    return s[best[1]:best[2]+1] if best[0]!=float('inf') else ""

def longest_unique(s):
    """Longest substring without repeating chars
    Time: O(n) | Space: O(min(n,charset))
    """
    seen={}; l=best=0
    for r,c in enumerate(s):
        if c in seen and seen[c]>=l: l=seen[c]+1
        seen[c]=r; best=max(best,r-l+1)
    return best

if __name__ == "__main__":
    print("="*55)
    print("  DSA Strings Toolkit — Project Lab India")
    print("="*55)
    print(f"  LongestPalindrome('babad')      = {longest_palindrome('babad')}")
    print(f"  KMP('AABAACAADAABAABA','AABA')  = {kmp_search('AABAACAADAABAABA','AABA')}")
    print(f"  GroupAnagrams                    = {group_anagrams(['eat','tea','tan','ate','nat','bat'])}")
    print(f"  MinWindow('ADOBECODEBANC','ABC') = {min_window('ADOBECODEBANC','ABC')}")
    print(f"  LongestUnique('abcabcbb')        = {longest_unique('abcabcbb')}")
    print("="*55)
```

---

## ⏱️ Complexity Reference Table

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|---------|
| Palindrome (expand) | O(n²) | O(1) | Substring palindrome |
| Manacher's | O(n) | O(n) | Optimal palindrome |
| KMP | O(n+m) | O(m) | Single pattern search |
| Rabin-Karp | O(n+m) avg | O(1) | Multiple pattern search |
| Z-Algorithm | O(n+m) | O(n) | Pattern + Z-array |
| Group Anagrams | O(n·k log k) | O(nk) | Anagram grouping |
| Min Window | O(n) | O(1) | Window problems |

---

## 📚 Learning Notes

### 🔑 Key Insights

1. **KMP LPS Array** — The failure function tells us where to jump when mismatch occurs. Never re-examine matched characters.
2. **Rolling Hash (Rabin-Karp)** — `hash(s[i+1..i+m]) = (hash(s[i..i+m-1]) - s[i]·base^(m-1)) · base + s[i+m]`
3. **Anagram Key** — Sorted string or character frequency tuple uniquely identifies an anagram group.
4. **Sliding Window on Strings** — Two pointers + frequency map. Expand right, shrink left when condition violated.
5. **Palindrome Center** — Every palindrome has a center (char or gap). Expand outward from center.

---

## 🎯 Top Interview Questions

1. Explain KMP algorithm. What is the LPS array and how is it built?
2. What is the difference between KMP and Rabin-Karp? When would you prefer each?
3. How do you check if two strings are anagrams in O(n)?
4. What is the Z-algorithm? How does it differ from KMP?
5. How would you find the longest palindromic substring in O(n) (Manacher's)?
6. Explain the sliding window approach for minimum window substring.
7. How do you handle Unicode characters vs ASCII in string problems?
8. What is the rolling hash technique? How does it avoid hash collisions?
9. How would you implement `strstr()` from scratch?
10. What is the suffix array? When is it better than KMP?

---

## ⚠️ Edge Cases to Always Check

- Empty string `""` — return empty or 0
- Single character — it's always a palindrome
- All same characters `"aaaa"` — all substrings are palindromes
- Pattern longer than text in KMP — return empty
- Unicode strings — use character codes carefully
- Case sensitivity — clarify with interviewer
- Spaces in strings — clarify if counted as characters
- Null/None input — guard clauses first

---

## 🧪 Test Cases

```python
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
```

---

## 📦 Project Structure

```
DSA-Strings-Interview-Toolkit/
├── solutions/
│   ├── main.py             ← All core solutions
│   ├── palindrome.py       ← Palindrome variants
│   ├── kmp.py              ← KMP + LPS array
│   ├── rabin_karp.py       ← Rolling hash
│   ├── z_algorithm.py      ← Z-array
│   └── anagram.py          ← Anagram problems
├── tests/
│   └── test_strings.py
├── notes/
│   └── string_tricks.md
├── problems/
│   └── problem_list.md
└── README.md
```

---

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/kushagrabansal-IOT/DSA-Strings-Interview-Toolkit.git
cd DSA-Strings-Interview-Toolkit

# Run solutions
python solutions/main.py

# Run tests
python -m pytest tests/ -v
```

---

## 🚀 Future Improvements

- [ ] Add Aho-Corasick for multi-pattern search
- [ ] Add Suffix Array + LCP implementation
- [ ] Add Boyer-Moore algorithm
- [ ] Add Manacher's O(n) palindrome
- [ ] Add trie-based string problems
- [ ] Add regex engine from scratch

---

## 📄 License

MIT License — Free to use, modify, distribute.

---

## 👨‍💻 Author

**Kushagra Bansal** — Founder @ Project Lab India, Jaipur
🔬 DSA • OOPS • DBMS • IoT • Competitive Programming
🏆 Innovation Award Recipient | IEEE Member
🛒 [radiomarket.in](https://radiomarket.in)

---

> ⭐ **Star this repo** if it helped your interview prep!
> 🍴 **Fork it** — add your own solutions!
> 📢 **Share it** — help other developers!
