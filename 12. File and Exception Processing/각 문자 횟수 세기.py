filename = input('파일명을 입력하세요: ').strip()
infile = open(filename, "r") # 파일을 연다.

freqs = {}

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다.
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
            # 딕셔너리에 있으면 하나 증가
        else:
            freqs[char] = 1
            # 딕셔너리에 없으면 1로 초기화
print(freqs)
infile.close()
