if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())
    # print(arr)
    # # maximum=max(arr)
    # mod_array =[]
    # for i in arr :
    #     if (i!=maximum) :
    #         mod_array=mod_array.append(i)
    # runner mod= max(mod_array)
    # print(runner)
    # import re
    # regex = r"([a-zA-Z]+) \d+"
    # matches = re.finditer(regex, "June 24, August 9, Dec 12")
    # for match in matches:
    #         # This will now print:
    #         #   June
    #         #   August
    #         #   Dec
    #     print("Match month: %s, %s" % (match.start(), match.end()))
    n = int(input())
    list1 = [input().split() for i in range(n)]
    print (list1)
