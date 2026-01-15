from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Paper:

    pass
class publicationExample_ConferencePaper(Paper):

    pass
class publicationExample_WorkshopPaper(Paper):

    pass
class Publication:

    pass
class publicationExample_Other(Publication):

    pass
class publicationExample_Thesis(Publication):

    pass
class publicationExample_Paper(Publication):

    pass
class publicationExample_Books(Publication):

    pass
class publicationExample_Editorship(Publication):

    pass
class publicationExample_JournalArticle(Publication):

    pass
class publicationExample_Humanity:

    pass
class publicationExample_Publication(ABC):

    pass
class Human:

    pass
class publicationExample_Researcher(Human):

    pass
class publicationExample_Human:

    pass