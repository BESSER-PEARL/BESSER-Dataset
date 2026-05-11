from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EStructuralFeatureTreeElement:

    pass
class internal_treeproxy_EReferenceTreeElement(EStructuralFeatureTreeElement):

    pass
class treeproxy_internal_EObject:

    pass
class TreeElement:

    pass
class internal_treeproxy_EObjectTreeElement(TreeElement):

    pass
class internal_treeproxy_TreeElement(ABC):

    pass
class EObjectTreeElement:

    pass
class internal_treeproxy_EStructuralFeatureTreeElement(TreeElement):

    pass
class treeproxy_internal_EAttribute:

    pass
class internal_treeproxy_EAttributeTreeElement(EStructuralFeatureTreeElement):

    pass
class treeproxy_internal_EReference:

    pass