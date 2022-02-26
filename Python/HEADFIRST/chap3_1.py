found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

print(found)

found['e'] += 1

print(found)

for i in found:
    print(i, "was_found", found[i], "time(s)")
