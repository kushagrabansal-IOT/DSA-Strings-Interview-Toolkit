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