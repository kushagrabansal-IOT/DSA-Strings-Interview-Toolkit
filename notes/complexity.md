# Learning Notes — DSA-Strings-Interview-Toolkit

### 🔑 Key Insights

1. **KMP LPS Array** — The failure function tells us where to jump when mismatch occurs. Never re-examine matched characters.
2. **Rolling Hash (Rabin-Karp)** — `hash(s[i+1..i+m]) = (hash(s[i..i+m-1]) - s[i]·base^(m-1)) · base + s[i+m]`
3. **Anagram Key** — Sorted string or character frequency tuple uniquely identifies an anagram group.
4. **Sliding Window on Strings** — Two pointers + frequency map. Expand right, shrink left when condition violated.
5. **Palindrome Center** — Every palindrome has a center (char or gap). Expand outward from center.

## Complexity Reference

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|---------|
| Palindrome (expand) | O(n²) | O(1) | Substring palindrome |
| Manacher's | O(n) | O(n) | Optimal palindrome |
| KMP | O(n+m) | O(m) | Single pattern search |
| Rabin-Karp | O(n+m) avg | O(1) | Multiple pattern search |
| Z-Algorithm | O(n+m) | O(n) | Pattern + Z-array |
| Group Anagrams | O(n·k log k) | O(nk) | Anagram grouping |
| Min Window | O(n) | O(1) | Window problems |