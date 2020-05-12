import string

def xss(username):
    for char in username:
        if char in string.ascii_letters:
            continue
        elif(ord(char)>=ord('0') and ord(char)<=ord('9')):
            continue
        elif(ord(char)==ord('_')):
            continue
        elif(ord(char)==ord(' ')):
            return "Username can not contain space"
        else:
            return "Username can not contain invalid special characters (Valid:_)"
    return 'True'

strings = []
strings.append('\x6a\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3a\x61\x6c\x65\x72\x74\x281337\x29')
strings.append('%27%5Cx6a%5Cx61%5Cx76%5Cx61%5Cx73%5Cx63%5Cx72%5Cx69%5Cx70%5Cx74%5Cx3a%5Cx61%5Cx6c%5Cx65%5Cx72%5Cx74%5Cx281337%5Cx29%27')

for string1 in strings:
    print('string ', xss(string1))