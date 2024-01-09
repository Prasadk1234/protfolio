def epc(st, left, right):
    max_l = 0
    sub_st = ''

    while left <= 0 and right < len(s) and st[right] == st[left]:

        if right - left + 1 > max_l:
            max_l = right - left + 1
            sub_st = st[left:right + 1]

        left -= 1
        right += 1
    return sub_st

s='babad'
result = ''
for i in range(len(s)):
    odd = epc(st=s,left=1, right=1)
    even = epc(st=s,left=1, right=1 + 1)

    if len(odd) > len(result):
        result = odd
    if len(even) > len(result):
        result = even
    print(odd,even)
print(result)

# Assign Cookies

def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    i = 0
    j = 0

    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            i += 1
            j += 1
        else:
            i += 1
    return j