from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Comment:

    pass
class mtpusecase_ConstraintComment(Comment):

    pass
class UseCase:

    pass
class mtpusecase_RequirementUseCase(UseCase):

    pass
class Actor:

    pass
class mtpusecase_TransformationActor(Actor):

    pass
class Relation:

    pass
class mtpusecase_Association(Relation):

    def __init__(self, targetName: str, sourceName: str):
        self.targetName = targetName
        self.sourceName = sourceName
        
        pass
    @property
    def targetName(self):
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName


    @property
    def sourceName(self):
        return self.__sourceName

    @sourceName.setter
    def sourceName(self, sourceName: str):
        self.__sourceName = sourceName


class mtpusecase_DirectedAssociation(Relation):

    def __init__(self, targetName: str):
        self.targetName = targetName
        
        pass
    @property
    def targetName(self):
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName


class HasInheritance:

    pass
class mtpusecase_Actor(HasInheritance):

    pass
class mtpusecase_UseCase(HasInheritance):

    pass
class PackableElement:

    pass
class mtpusecase_Include(PackableElement):

    pass
class mtpusecase_Relation(PackableElement):

    pass
class mtpusecase_Comment(PackableElement):

    pass
class mtpusecase_Extend(PackableElement):

    pass
class mtpusecase_Generalization(PackableElement):

    pass
class mtpusecase_HasInheritance(PackableElement):

    pass
class NamedElement:

    pass
class mtpusecase_PackableElement(NamedElement):

    pass
class mtpusecase_Package(NamedElement):

    pass
class mtpusecase_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

