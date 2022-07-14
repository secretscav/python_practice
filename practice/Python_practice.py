# class Meta(type):
#     def __init__(self, class_name, bases, attributes)
class God(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        # information = {}
        # for item, value in attrs.items():
        #     if item.startswith("__"):
        #         information[item] = value
        #     else:
        #         information[item.uper()] = value
        # print(information)
        return type(class_name, bases, attrs)


class Mamals(metaclass=God):
    # def __init__(self, firstName:str, lastName:str, age:int) -> complex:
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.age = age

    # def __repr__(self):
    #     print(f"{self.__name__}")
    x = 34
    y = 12

first = Mamals()

