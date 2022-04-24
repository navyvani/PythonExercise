list1 = ["aabbc", "aabbcc", "abcabcd", "bad", "dog", "kill", "superb"]
list2 = ["bbaad", "aabbcd", "abcabde", "dad", "god", "killl", "superr"]

d1 = {}
d2 = {}

# for l1, l2 in zip(list1, list2):
#     if len(l1) == len(l2):
#         for
dl1 = {}
dl2 = {}
for i in range(len(list1)):
    dl1 = {}
    dl2 = {}
    if len(list1[i]) == len(list2[i]):
        for j,k in zip(list1[i], list2[i]):
            if dl1.get(j):
                dl1[j] +=1
            else:
                dl1[j] =1

            if dl2.get(k):
                dl2[k] +=1
            else:
                dl2[k] =1

        diff_count = 0
        keys_of_dl1 = list(dl1.keys())
        keys_of_dl2 = list(dl2.keys())

        for x in keys_of_dl1:
            if x not in keys_of_dl2 or abs(dl1[x]-dl2[x]) != 0 :
                diff_count += 1
                if abs(dl1[x]-dl2[x]) >= 1:
                    diff_count += abs(dl1[x]-dl2[x])
                    break
            # if x not in keys_of_dl2

        if diff_count == 1:
            print(list1[i], list2[i])


        # d1[i] = {}
        # d2[i] = {}
        # for j,k in zip(list1[i], list2[i]):
        #     if d1[i].get(j):
        #         d1[i][j] += 1
        #     else:
        #         d1[i][j] = 1
        #
        #     if d2[i].get(k):
        #         d2[i][k] += 1
        #     else:
        #         d2[i][k] = 1
        #

