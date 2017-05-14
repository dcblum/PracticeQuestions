

# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function returns
# True. Your function definition should look like: question1(s, t) and return a
# boolean True or False.

def question1(s,t):
    if t in s:
        return True
    for i in range(len(s)):
        t_list = list(t)
        for j in s[i:]:
            if j in t_list:
                t_list.remove(j)
                if t_list == []:
                    return True

    return False

########################################################################
#
#                   TESTS
#
########################################################################



s1 = 'supercalifragilisticexpialidocious'
t1 = 'codious'

s2 = '1'
t2 = ''

s3 = 'abc123'
t3 = 'def456'

s4 = ''
t4 = ''

print question1(s1,t1)
# True

print question1(s2,t2)
# True

print question1(s3,t3)
# False

print question1(s4,t4)
# True
