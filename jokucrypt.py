

letters = "abcdefghijklmnopqrstuvwxyz"
cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
specials = "^¨'*-_.:,;<>|!# ¤%&/()=?@£$€{[]}"

def changeletter(letter, key):
    x = letters.index(letter)
    x = (x + key) % len(letters)
    return letters[x]




def changenumber(number, key):
    x = nums.index(number)
    x = (x + key) % len(nums)
    return nums[x]

def changecapitalletter(letter, key):
    x = cap_letters.index(letter)
    x = (x + key) % len(cap_letters)
    return cap_letters[x]


def rchangeletter(letter, key):
    x = letters.index(letter)
    x = (x - key) % len(letters)
    return letters[x]

def rchangenumber(number, key):
    x = nums.index(number)
    x = (x + key) % len(nums)
    return nums[x]

def rchangecapitalletter(letter, key):
    x = cap_letters.index(letter)
    x = (x - key) % len(cap_letters)
    return cap_letters[x]

def changespecial(letter, key):
    x = specials.index(letter)
    x = (x + key) % len(specials)
    return specials[x]
def rchangespecial(letter, key):
    x = specials.index(letter)
    x = (x - key) % len(specials)
    return specials[x]



def encrypt(text, key):
    completed = ""
    for i in text:
        if i.isdigit():
            completed += changenumber(i, key)

        elif i.isalpha():
            if i.isupper():
                completed += changecapitalletter(i, key)
            else:

                completed += changeletter(i, key)


        else:
            completed += changespecial(i, key)


    return completed


def decrypt(text, key):
    completed = ""
    for i in text:
        if i.isdigit():
            completed += rchangenumber(i, key)
        elif i.isalpha():
            if i.isupper():
                completed += rchangecapitalletter(i, key)
            else:
                completed += rchangeletter(i, key)
        else:
            completed += rchangespecial(i, key)
    return completed



x = encrypt("Vitun homo neekeri", 4)
print(x)
y = decrypt(x, 4)
print(y)
