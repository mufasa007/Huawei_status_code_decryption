class Test(object):
    def __init__(self, title):  #可定义多个参数
        self.title = title
    def get_title(self):   #定义了实例方法
        return self.title
    @classmethod
    def get_time(cls):  #定义了类方法
        print("On July 2")
    @staticmethod
    def get_grade():      #定义了静态方法
        print("89")

MS = Test('Molecular system examination')

d0 = MS.get_title();  #通过实例调用
d1 = Test.get_title(MS)  #通过类的方式调用

pass