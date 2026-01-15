from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class core_CORECompositionSpecification(ABC):

    pass
class core_COREMapping:

    pass
class CORECompositionSpecification:

    pass
class core_COREPattern(CORECompositionSpecification):

    pass
class core_COREBinding(CORECompositionSpecification):

    pass
class core_CORENamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class CORENamedElement:

    pass
class core_COREConfiguration(CORENamedElement):

    pass
class core_COREStrategy(CORENamedElement):

    pass
class core_COREModel(CORENamedElement):

    pass
class COREModelElement:

    pass
class core_COREImpactModelElement(COREModelElement):

    pass
class core_COREInterface:

    pass
class core_COREConcern(CORENamedElement):

    pass
class COREModel:

    pass
class core_COREFeatureModel(COREModel):

    pass
class core_COREImpactModel(COREModel):

    pass
class core_COREFeature(COREModelElement):

    pass
class core_COREModelElement(CORENamedElement):

    pass
class core_COREReuse:

    pass