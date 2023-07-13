# 类字段显示类的信息，实例字段显示实例的信息
# 类是具有相同属性和方法的一群对象的集合
class Cat:
    total_cat_number = 0  # 类字段
    hungry = False

    def __init__(self, name, age, isfish=False):
        self.name = name  # 实例字段
        self.age = age
        self.isfish = isfish

        Cat.total_cat_number += 1

    def eat(self, food='fish'):
        print(f'{self.name} eatting {food}...')
        if Cat.total_cat_number > 1:
            print(f"{self.name}没有足够的小鱼吃啦...")
            Cat.hungry = True

        if food == 'fish':
            self.isfish = True
        else:
            self.isfish = False

    def sleep(self):
        print(f'{self.name} sleepping...')


def main():
    cat1 = Cat('catte', 3)
    print(f'这一群猫猫挨饿了吗？ {Cat.hungry}')
    cat1.eat('fish')
    print(f'{cat1.name}是否吃的是小鱼干? {cat1.isfish}')

    cat2 = Cat('biter', 1)
    cat2.sleep()
    cat2.eat('cake')
    print(f'{cat2.name}是否吃的是小鱼干? {cat2.isfish}')
    print(f'这一群猫猫挨饿了吗？ {Cat.hungry}')
    print(f'总计来了{Cat.total_cat_number}只猫猫')


if __name__ == "__main__":
    main()
