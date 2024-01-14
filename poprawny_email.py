def PoprawnyEmail(email):
    dl = len(email)

    # etap 1
    i = 0
    while email[i] != '@' and i < dl-1:
        i += 1
    if email[i] != '@' or i < 1: # i < 1 ilośc liter po lewej stronie małpy
        return False
    # etap 2
    k = dl - 1
    while email[k] != '.' and k > 0:
        k = k - 1
    if email[k] != '.' or not (k == dl - 3 or k == dl - 4):
        return False
    #etap 3
    if k - i <= 1:
        return False
    return True

print(PoprawnyEmail('a@m.pl'))

#do dokończnia 