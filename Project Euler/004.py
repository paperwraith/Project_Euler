
def reverse_num(num):
    rev_num = 0
    while num > 0:
        remainder = num % 10
        rev_num = (rev_num * 10) + remainder
        num = num // 10
    return rev_num


def pal_check(product, rev_num):
    chk = False
    if product == rev_num:
        chk = True
    return chk


def make_list():
    x = []
    for i in range(100, 1000):
        x.append(i)
    return x


def get_pal(x, y):
    for i in x:
        for j in y:
            product = i * j
            rev_num = reverse_num(product)
            if pal_check(product, rev_num) is True:
                pal = product
    return pal


x = make_list()
y = make_list()
print(get_pal(x, y))
