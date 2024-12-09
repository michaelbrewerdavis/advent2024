def parse(lines):
    return list(map(int, list(lines[0])))


def expand(compacted):
    expanded = []
    for i, n in enumerate(compacted):
        fileId = int(i / 2) if i % 2 == 0 else None
        expanded += [fileId] * n
    return expanded


def defrag(drive):
    drive = drive[::]
    left = 0
    right = len(drive) - 1

    while left < right:
        while drive[left] is not None:
            left += 1
        while drive[right] is None:
            right -= 1
        if left < right:
            drive[left], drive[right] = drive[right], drive[left]
        left += 1
        right -= 1
    return drive


def checksum(drive):
    sum = 0
    for i, n in enumerate(drive):
        if n is None:
            continue
        sum += i * n
    return sum


def expand2(compacted):
    expanded = []
    for i, n in enumerate(compacted):
        if n == 0:
            continue
        fileId = int(i / 2) if i % 2 == 0 else None
        expanded.append((fileId, n))
    return expanded


def defragStep(drive, fileId):
    pos, block = next((i, block) for i, block in enumerate(drive) if block[0] == fileId)
    i = 0
    while i < pos:
        if drive[i][0] is None:
            if (diff := drive[i][1] - block[1]) >= 0:
                drive[i] = block
                drive[pos] = (None, block[1])
                if diff > 0:
                    drive.insert(i + 1, (None, diff))
                return
        i += 1


def defrag2(drive):
    maxFileId = next(block[0] for block in reversed(drive) if block[0] is not None)
    for id in range(maxFileId, -1, -1):
        defragStep(drive, id)

    return drive


def checksum2(drive):
    pos = 0
    sum = 0
    for fileId, len in drive:
        if fileId is not None:
            for i in range(len):
                sum += fileId * (pos + i)
        pos += len
    return sum


def run(input):
    drive = expand(input)
    defragged = defrag(drive)
    print(checksum(defragged))

    drive2 = expand2(input)
    defragged2 = defrag2(drive2)
    print(checksum2(defragged2))
