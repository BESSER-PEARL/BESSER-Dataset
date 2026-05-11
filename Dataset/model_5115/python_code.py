from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SuperClass:

    pass
class SuperSuperClass:

    pass
class testPackage_DerivedClass(SuperClass, SuperSuperClass):

    pass
class testPackage_SuperClass(SuperSuperClass):

    pass
class testPackage_SuperSuperClass:

    pass