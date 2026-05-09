from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Entity:

    pass
class graphmodelling_Node(Entity):

    pass
class graphmodelling_Edge(Entity):

    pass
class graphmodelling_Property(Entity):

    pass
class graphmodelling_Operation(Entity):

    pass
class graphmodelling_Graph(Entity):

    pass
class graphmodelling_Entity:

    def __init__(self, ID: str, name: str, text: str, description: str, value: str, type: str, className: str, group: str, category: str, accessModifier: str, x: str, y: str, width: str, height: str):
        self.ID = ID
        self.name = name
        self.text = text
        self.description = description
        self.value = value
        self.type = type
        self.className = className
        self.group = group
        self.category = category
        self.accessModifier = accessModifier
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def accessModifier(self):
        return self.__accessModifier

    @accessModifier.setter
    def accessModifier(self, accessModifier: str):
        self.__accessModifier = accessModifier


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


class graphmodelling_ModellingType:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

