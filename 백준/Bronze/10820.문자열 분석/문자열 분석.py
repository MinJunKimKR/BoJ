# 12:51 -> 1:21
import sys
sys_input = sys.stdin.readlines


for line in sys.stdin:
    words = list(line)
    cnt = [0, 0, 0, 0]
    for word in words:
        if word == '\n':
            break
        askii_code = ord(word)
        if askii_code == 32:
            cnt[3] += 1
            continue
        if askii_code < 65:
            cnt[2] += 1
            continue
        if askii_code < 97:
            cnt[1] += 1
            continue
        if askii_code > 96:
            cnt[0] += 1
            continue
    print(' '.join(map(str, cnt)))
