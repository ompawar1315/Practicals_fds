s = input("Enter string: ")
word = input("Word: ")
def length_str(s):
    count = 0
    for _ in s:
        count=count+1
    return count
print(f"Length of word is: {length_str(word)} ")
length_str(s)

def longest_len(s):
    l = s.split()
    count = 0
    temp = l[0]
    for i in s:
        if(len(i) > count):
            count = len(i)
            temp = i
    print("Word with longest length is: ",temp)
    return(temp, count)
longest_len(s) 

def check_palindrome(s):
    if s == s[::-1]:
        return True
    return False
print(f"Given {word} is palindrome or not: {check_palindrome(word)}")
check_palindrome(s)

def appearance(s, subs):
    if subs in s:
        s = s.split(subs)
        return len(s[0])
print(f"Index of the first appearance of the substring is: {appearance(s, word)}")
appearance(s, word)
