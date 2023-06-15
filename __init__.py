'''def sTr(s):
    for sum in set(s):
        counter = 0
        for sub_sum in s:
            if sum == sub_sum:
                counter += 1
        print(sum, counter)

sTr("hfghjkdovjvjjdkjdo")'''






def sTr(s):
    sus = {}
    for sum in (s):
        sus[sum] = sus.get(sum, 0) + 1

    for sum, count in sus.items() :
        print(sum, count)
sTr("hfghjkdovjvjjdkjdo")