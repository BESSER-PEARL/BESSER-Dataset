####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
BookStorage_Interface = Class(name="BookStorage_Interface")
OwnBookStorage = Class(name="OwnBookStorage")
InnerBookStorage = Class(name="InnerBookStorage")
PaymentByCard1 = Class(name="PaymentByCard1")
BankAccount = Class(name="BankAccount")
ClassA = Class(name="ClassA")
ClassB = Class(name="ClassB")
ClassC = Class(name="ClassC")
ClassD = Class(name="ClassD")
ClassE = Class(name="ClassE")
ClassF = Class(name="ClassF")
ClassG = Class(name="ClassG")
ClassJ = Class(name="ClassJ")
ClassH = Class(name="ClassH")
ClassK = Class(name="ClassK")
ClassL = Class(name="ClassL")
ClassM = Class(name="ClassM")
ClassN = Class(name="ClassN")
ClassP = Class(name="ClassP")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
ClassQ = Class(name="ClassQ")
ClassR = Class(name="ClassR")
ClassS = Class(name="ClassS")
ClassT = Class(name="ClassT")
ClassU = Class(name="ClassU")
ClassV = Class(name="ClassV")
______Actor = Class(name="______Actor")
_______________UseCase = Class(name="_______________UseCase")
__________________UseCase = Class(name="__________________UseCase")
______________UseCase = Class(name="______________UseCase")
___________________________UseCase = Class(name="___________________________UseCase")
________________________Component = Class(name="________________________Component")
______________________________Component = Class(name="______________________________Component")
__________Component = Class(name="__________Component")
___________________________Component = Class(name="___________________________Component")
________________Component = Class(name="________________Component")
______________________Component = Class(name="______________________Component")
_________________________Component = Class(name="_________________________Component")
Coward = Class(name="Coward")
EnemyStrategy_Interface = Class(name="EnemyStrategy_Interface")
Brave = Class(name="Brave")
NotMyBusiness = Class(name="NotMyBusiness")
Items = Class(name="Items")
Armor = Class(name="Armor")
Knife = Class(name="Knife")
Actor = Class(name="Actor")
Inventory = Class(name="Inventory")
Inventory1 = Class(name="Inventory1")
Stats = Class(name="Stats")
PlayerActor = Class(name="PlayerActor")
WallActor = Class(name="WallActor")
Screen_Interface = Class(name="Screen_Interface")
GameScreen = Class(name="GameScreen")
MenuScreen = Class(name="MenuScreen")
Map = Class(name="Map")
Hero = Class(name="Hero")
MazeGenerator = Class(name="MazeGenerator")
LevelMap = Class(name="LevelMap")
MapGenerator = Class(name="MapGenerator")
StateService = Class(name="StateService")
Point = Class(name="Point")
book = Class(name="book")
Client = Class(name="Client")
SystemUser_Interface = Class(name="SystemUser_Interface")
Admin = Class(name="Admin")
ShopAPI = Class(name="ShopAPI")
PaymentByCard = Class(name="PaymentByCard")
Payment_Interface = Class(name="Payment_Interface")
Basket = Class(name="Basket")
Order = Class(name="Order")
PaymentByAccaunt = Class(name="PaymentByAccaunt")
Client_hoice_Interface = Class(name="Client_hoice_Interface")
Wishlist = Class(name="Wishlist")
Catalog = Class(name="Catalog")
SearchRequest = Class(name="SearchRequest")
ClientDatabase = Class(name="ClientDatabase")
DatabaseAPI = Class(name="DatabaseAPI")
Review_Interface = Class(name="Review_Interface")
ClientRewiev = Class(name="ClientRewiev")
OriginalReview = Class(name="OriginalReview")
ShortReview = Class(name="ShortReview")
DetailDescription = Class(name="DetailDescription")

# BookStorage_Interface class attributes and methods

# OwnBookStorage class attributes and methods

# InnerBookStorage class attributes and methods

# PaymentByCard1 class attributes and methods

# BankAccount class attributes and methods
BankAccount_ownerName: Property = Property(name="ownerName", type=StringType)
BankAccount_balance: Property = Property(name="balance", type=FloatType)
BankAccount.attributes={BankAccount_ownerName, BankAccount_balance}

# ClassA class attributes and methods
ClassA_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassA_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassA_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassA_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassA.attributes={ClassA_privateAttribute, ClassA_protectedAttribute, ClassA_packageAttribute, ClassA_publicAttribute}

# ClassB class attributes and methods

# ClassC class attributes and methods
ClassC_publicAttribute: Property = Property(name="publicAttribute", type=FloatType)
ClassC_privateAttribute: Property = Property(name="privateAttribute", type=IntegerType)
ClassC_protectedAttribute: Property = Property(name="protectedAttribute", type=StringType)
ClassC_packageAttribute: Property = Property(name="packageAttribute", type=StringType)
ClassC.attributes={ClassC_publicAttribute, ClassC_privateAttribute, ClassC_protectedAttribute, ClassC_packageAttribute}

# ClassD class attributes and methods

# ClassE class attributes and methods

# ClassF class attributes and methods

# ClassG class attributes and methods

# ClassJ class attributes and methods

# ClassH class attributes and methods

# ClassK class attributes and methods

# ClassL class attributes and methods

# ClassM class attributes and methods

# ClassN class attributes and methods

# ClassP class attributes and methods

# InterfaceO_Interface class attributes and methods

# ClassQ class attributes and methods

# ClassR class attributes and methods

# ClassS class attributes and methods

# ClassT class attributes and methods

# ClassU class attributes and methods

# ClassV class attributes and methods

# ______Actor class attributes and methods

# _______________UseCase class attributes and methods

# __________________UseCase class attributes and methods

# ______________UseCase class attributes and methods

# ___________________________UseCase class attributes and methods

# ________________________Component class attributes and methods

# ______________________________Component class attributes and methods

# __________Component class attributes and methods

# ___________________________Component class attributes and methods

# ________________Component class attributes and methods

# ______________________Component class attributes and methods

# _________________________Component class attributes and methods

# Coward class attributes and methods

# EnemyStrategy_Interface class attributes and methods

# Brave class attributes and methods

# NotMyBusiness class attributes and methods

# Items class attributes and methods

# Armor class attributes and methods

# Knife class attributes and methods

# Actor class attributes and methods

# Inventory class attributes and methods

# Inventory1 class attributes and methods

# Stats class attributes and methods

# PlayerActor class attributes and methods

# WallActor class attributes and methods

# Screen_Interface class attributes and methods

# GameScreen class attributes and methods

# MenuScreen class attributes and methods

# Map class attributes and methods

# Hero class attributes and methods

# MazeGenerator class attributes and methods

# LevelMap class attributes and methods

# MapGenerator class attributes and methods

# StateService class attributes and methods

# Point class attributes and methods

# book class attributes and methods
book_title: Property = Property(name="title", type=StringType)
book_author: Property = Property(name="author", type=StringType)
book_keywords: Property = Property(name="keywords", type=StringType)
book_catygory: Property = Property(name="catygory", type=StringType)
book_rate: Property = Property(name="rate", type=FloatType)
book.attributes={book_keywords, book_title, book_rate, book_catygory, book_author}

# Client class attributes and methods
Client_name: Property = Property(name="name", type=StringType)
Client_addres: Property = Property(name="addres", type=StringType)
Client_card: Property = Property(name="card", type=StringType)
Client.attributes={Client_name, Client_card, Client_addres}

# SystemUser_Interface class attributes and methods

# Admin class attributes and methods

# ShopAPI class attributes and methods

# PaymentByCard class attributes and methods

# Payment_Interface class attributes and methods

# Basket class attributes and methods

# Order class attributes and methods

# PaymentByAccaunt class attributes and methods

# Client_hoice_Interface class attributes and methods

# Wishlist class attributes and methods

# Catalog class attributes and methods

# SearchRequest class attributes and methods

# ClientDatabase class attributes and methods

# DatabaseAPI class attributes and methods

# Review_Interface class attributes and methods

# ClientRewiev class attributes and methods
ClientRewiev_mark: Property = Property(name="mark", type=IntegerType)
ClientRewiev_text: Property = Property(name="text", type=StringType)
ClientRewiev.attributes={ClientRewiev_text, ClientRewiev_mark}

# OriginalReview class attributes and methods
OriginalReview_texr: Property = Property(name="texr", type=StringType)
OriginalReview.attributes={OriginalReview_texr}

# ShortReview class attributes and methods

# DetailDescription class attributes and methods

# Relationships
book_ShortReview: BinaryAssociation = BinaryAssociation(
    name="book_ShortReview",
    ends={
        Property(name="shortReview26", type=ShortReview, multiplicity=Multiplicity(0, 1)),
        Property(name="book27", type=book, multiplicity=Multiplicity(0, 1))
    }
)
Catalog_book: BinaryAssociation = BinaryAssociation(
    name="Catalog_book",
    ends={
        Property(name="book28", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="catalog29", type=Catalog, multiplicity=Multiplicity(0, 1))
    }
)
Client_ClientDatabase: BinaryAssociation = BinaryAssociation(
    name="Client_ClientDatabase",
    ends={
        Property(name="clientDatabase30", type=ClientDatabase, multiplicity=Multiplicity(0, 1)),
        Property(name="client31", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
Catalog_OwnBookStorage: BinaryAssociation = BinaryAssociation(
    name="Catalog_OwnBookStorage",
    ends={
        Property(name="ownBookStorage32", type=OwnBookStorage, multiplicity=Multiplicity(0, 1)),
        Property(name="catalog33", type=Catalog, multiplicity=Multiplicity(0, 1))
    }
)
Catalog_InnerBookStorage: BinaryAssociation = BinaryAssociation(
    name="Catalog_InnerBookStorage",
    ends={
        Property(name="innerBookStorage34", type=InnerBookStorage, multiplicity=Multiplicity(0, 1)),
        Property(name="catalog35", type=Catalog, multiplicity=Multiplicity(0, 1))
    }
)
Client_Order: BinaryAssociation = BinaryAssociation(
    name="Client_Order",
    ends={
        Property(name="order36", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="client37", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
SearchRequest_book: BinaryAssociation = BinaryAssociation(
    name="SearchRequest_book",
    ends={
        Property(name="book38", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="searchRequest39", type=SearchRequest, multiplicity=Multiplicity(0, 1))
    }
)
SearchRequest_Catalog: BinaryAssociation = BinaryAssociation(
    name="SearchRequest_Catalog",
    ends={
        Property(name="catalog40", type=Catalog, multiplicity=Multiplicity(0, 1)),
        Property(name="searchRequest41", type=SearchRequest, multiplicity=Multiplicity(0, 1))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="payment42", type=Payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="order43", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Client_Payment: BinaryAssociation = BinaryAssociation(
    name="Client_Payment",
    ends={
        Property(name="payment44", type=Payment_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="client45", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
Client_Basket: BinaryAssociation = BinaryAssociation(
    name="Client_Basket",
    ends={
        Property(name="basket46", type=Basket, multiplicity=Multiplicity(0, 1)),
        Property(name="client47", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
Wishlist_book: BinaryAssociation = BinaryAssociation(
    name="Wishlist_book",
    ends={
        Property(name="book48", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="wishlist49", type=Wishlist, multiplicity=Multiplicity(0, 1))
    }
)
Basket_book: BinaryAssociation = BinaryAssociation(
    name="Basket_book",
    ends={
        Property(name="book50", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="basket51", type=Basket, multiplicity=Multiplicity(0, 1))
    }
)
Order_book: BinaryAssociation = BinaryAssociation(
    name="Order_book",
    ends={
        Property(name="book52", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="order53", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Client_Wishlist: BinaryAssociation = BinaryAssociation(
    name="Client_Wishlist",
    ends={
        Property(name="wishlist54", type=Wishlist, multiplicity=Multiplicity(0, 1)),
        Property(name="client55", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassE: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE",
    ends={
        Property(name="classE0", type=ClassE, multiplicity=Multiplicity(0, 1)),
        Property(name="classD1", type=ClassD, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopy",
    ends={
        Property(name="classG2", type=ClassG, multiplicity=Multiplicity(0, 1)),
        Property(name="classF3", type=ClassF, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassECopyCopy: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassECopyCopy",
    ends={
        Property(name="classG4", type=ClassJ, multiplicity=Multiplicity(0, 1)),
        Property(name="classF5", type=ClassH, multiplicity=Multiplicity(0, 1))
    }
)
____________________: BinaryAssociation = BinaryAssociation(
    name="____________________",
    ends={
        Property(name="______________6", type=_______________UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="_____7", type=______Actor, multiplicity=Multiplicity(0, 1))
    }
)
_______________________: BinaryAssociation = BinaryAssociation(
    name="_______________________",
    ends={
        Property(name="_________________8", type=__________________UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="_____9", type=______Actor, multiplicity=Multiplicity(0, 1))
    }
)
___________________: BinaryAssociation = BinaryAssociation(
    name="___________________",
    ends={
        Property(name="_____________10", type=______________UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="_____11", type=______Actor, multiplicity=Multiplicity(0, 1))
    }
)
_________________________________________: BinaryAssociation = BinaryAssociation(
    name="_________________________________________",
    ends={
        Property(name="__________________________12", type=___________________________UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="______________13", type=_______________UseCase, multiplicity=Multiplicity(0, 1))
    }
)
____________________________________________: BinaryAssociation = BinaryAssociation(
    name="____________________________________________",
    ends={
        Property(name="__________________________14", type=___________________________UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="_________________15", type=__________________UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_Basket: BinaryAssociation = BinaryAssociation(
    name="Order_Basket",
    ends={
        Property(name="basket16", type=Basket, multiplicity=Multiplicity(0, 1)),
        Property(name="order17", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
book_Review: BinaryAssociation = BinaryAssociation(
    name="book_Review",
    ends={
        Property(name="review18", type=Review_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="book19", type=book, multiplicity=Multiplicity(0, 1))
    }
)
book_DetailDescription: BinaryAssociation = BinaryAssociation(
    name="book_DetailDescription",
    ends={
        Property(name="detailDescription20", type=DetailDescription, multiplicity=Multiplicity(0, 1)),
        Property(name="book21", type=book, multiplicity=Multiplicity(0, 1))
    }
)
DetailDescription_ClientRewiev: BinaryAssociation = BinaryAssociation(
    name="DetailDescription_ClientRewiev",
    ends={
        Property(name="clientRewiev22", type=ClientRewiev, multiplicity=Multiplicity(0, 1)),
        Property(name="detailDescription23", type=DetailDescription, multiplicity=Multiplicity(0, 1))
    }
)
DetailDescription_OriginalReview: BinaryAssociation = BinaryAssociation(
    name="DetailDescription_OriginalReview",
    ends={
        Property(name="originalReview24", type=OriginalReview, multiplicity=Multiplicity(0, 1)),
        Property(name="detailDescription25", type=DetailDescription, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5c7cf1d5_8cef_455c_a5bc_62cfc74d44a2",
    types={BookStorage_Interface, OwnBookStorage, InnerBookStorage, PaymentByCard1, BankAccount, ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassJ, ClassH, ClassK, ClassL, ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, ______Actor, _______________UseCase, __________________UseCase, ______________UseCase, ___________________________UseCase, ________________________Component, ______________________________Component, __________Component, ___________________________Component, ________________Component, ______________________Component, _________________________Component, Coward, EnemyStrategy_Interface, Brave, NotMyBusiness, Items, Armor, Knife, Actor, Inventory, Inventory1, Stats, PlayerActor, WallActor, Screen_Interface, GameScreen, MenuScreen, Map, Hero, MazeGenerator, LevelMap, MapGenerator, StateService, Point, book, Client, SystemUser_Interface, Admin, ShopAPI, PaymentByCard, Payment_Interface, Basket, Order, PaymentByAccaunt, Client_hoice_Interface, Wishlist, Catalog, SearchRequest, ClientDatabase, DatabaseAPI, Review_Interface, ClientRewiev, OriginalReview, ShortReview, DetailDescription},
    associations={book_ShortReview, Catalog_book, Client_ClientDatabase, Catalog_OwnBookStorage, Catalog_InnerBookStorage, Client_Order, SearchRequest_book, SearchRequest_Catalog, Order_Payment, Client_Payment, Client_Basket, Wishlist_book, Basket_book, Order_book, Client_Wishlist, ClassD_ClassE, ClassD_ClassECopy, ClassD_ClassECopyCopy, ____________________, _______________________, ___________________, _________________________________________, ____________________________________________, Order_Basket, book_Review, book_DetailDescription, DetailDescription_ClientRewiev, DetailDescription_OriginalReview},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)