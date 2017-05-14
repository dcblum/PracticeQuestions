
# Given a string a, find the longest palindromic substring contained in a. Your
# function definition should look like question2(a), and return a string.

def question2(a):
    ''''''
    longest = ''

    string = a
    chars = [' ', ',',':',';','.','!']
    for i in chars:
        string = string.replace(i, '')

    a_nospaces = string.lower()
    a_back_nospaces =  a_nospaces[::-1]

    if len(a_nospaces) < 2:
        return a
    if a_back_nospaces == a_nospaces:
        return a

    for i in range(len(a_nospaces)):
        for j in range(i,len(a_nospaces)):
            if a_nospaces[i:j+1] in a_back_nospaces:
                if len(a_nospaces[i:j+1]) > len(longest):
                    longest = a_nospaces[i:j+1]

    return longest

########################################################################
#
#                   TEST Question2
#
########################################################################


a0 = 'burgeregrub'
a1 = 'muzzle velocity'
a2 = ''
a3 = '1'
a4 = 'my favorite sport involves racecars'
a5 = 'There was a man, a plan, a canal: Panama'

print question2(a0)
# 'burgeregrub'

print question2(a1)
# 'level'

print question2(a2)
# ''

print question2(a3)
# '1'

print question2(a4)
# 'sracecars'

print question2(a5)
# 'amanaplanacanalpanama'
