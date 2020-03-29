def chk_anagram(str1, str2):

    if len(str1) == len(str2) and set(str1.lower()) == set(str2.lower()):
        return ''.join(sorted(str1.lower())) == ''.join(sorted(str2.lower()))
    return False


print(chk_anagram('aabb', 'AaBb'))
print('new line added')
print('added another line')