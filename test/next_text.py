#  参考文章 https://blog.csdn.net/qq_30193419/article/details/91442722
def all_even():
    n = 0
    while True:
        yield n
        n += 2


my_gen = all_even()

my_gen1 = all_even()


for i in range(5):
    print(next(my_gen))


for i in range(20):
    print(f'{next(my_gen)}----')
