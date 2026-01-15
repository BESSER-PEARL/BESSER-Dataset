from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EObjectTreeElement:

    pass
class treeproxy_internal_EAttribute:

    pass
class treeproxy_internal_EReference:

    pass
class EStructuralFeatureTreeElement:

    pass
class internal_treeproxy_EAttributeTreeElement(EStructuralFeatureTreeElement):

    pass
class internal_treeproxy_EReferenceTreeElement(EStructuralFeatureTreeElement):

    pass
class treeproxy_internal_EObject:

    pass
class TreeElement:

    pass
class internal_treeproxy_EStructuralFeatureTreeElement(TreeElement):

    pass
class internal_treeproxy_EObjectTreeElement(TreeElement):

    pass
class internal_treeproxy_TreeElement(ABC):

    pass