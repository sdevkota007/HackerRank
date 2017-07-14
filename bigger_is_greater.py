#find the next lexicographically bigger word
#written by Sudarshan Devkota

# num = int(input())
#
# str_list = [str(input()) for t in range(num)]
# for str in str_list:
#     full_string = str
#     #change the string to list of characters
#     char_list = [char for char in str]
#     break_out=False
#
#     i=1
#     for i in range(i, len(char_list)+1):
#
#         j=i
#         for j in range(j, len(char_list)+1):
#             if char_list[-i] > char_list[-j]:
#                 char_list[-i],char_list[-j] = char_list[-j],char_list[-i]
#                 break_out = True
#                 break
#
#
#         if break_out:
#             #sort in ascending order all the elements after the character char_list[-j]
#             first_string = "".join(char_list[:-(j-1)])
#             # print ("first_string ", first_string)
#
#             second_string = "".join(sorted(char_list[-(j-1):]))
#             # print ("second_string ", second_string)
#             full_string = first_string+second_string
#             break
#     if full_string != str:
#         print (full_string)
#     else:
#         print ("no answer")



#alternate solution : Better Solution
t = input()
for _ in range(t):
    word = list(raw_input().strip())
    start = -1
    for i in xrange(0, len(word) - 1):
        if word[i] < word[i + 1]:
            start = i

    if start == -1:
        print "no answer"
        continue

    end = -1
    for j in xrange(start + 1, len(word)):
        if word[start] < word[j]:
            end = j

    word[start], word[end] = word[end], word[start]
    a = word[start + 1:]
    a.sort()

    for j in xrange(start + 1, len(word)):
        word[j] = a[j - start - 1]

    print "".join(word)