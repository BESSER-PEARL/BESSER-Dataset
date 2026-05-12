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
datatypes_Documents = Class(name="datatypes_Documents")
datatypes_Json = Class(name="datatypes_Json")
datatypes_Number = Class(name="datatypes_Number")
datatypes_String = Class(name="datatypes_String")
datatypes_Bool = Class(name="datatypes_Bool")
datatypes_Array = Class(name="datatypes_Array")
datatypes_Value = Class(name="datatypes_Value", is_abstract=True)
user_Business = Class(name="user_Business")
user_User = Class(name="user_User")
user_Provider = Class(name="user_Provider")
user_Tags = Class(name="user_Tags")
marketing_Product = Class(name="marketing_Product")
marketing_Review = Class(name="marketing_Review")
system_Category = Class(name="system_Category")
Address = Class(name="Address")

# datatypes_Documents class attributes and methods
datatypes_Documents_file: Property = Property(name="file", type=StringType)
datatypes_Documents_data: Property = Property(name="data", type=datatypes_Json)
datatypes_Documents_file_name: Property = Property(name="file_name", type=StringType)
datatypes_Documents_tab_counter: Property = Property(name="tab_counter", type=IntegerType)
datatypes_Documents.attributes={datatypes_Documents_data, datatypes_Documents_file_name, datatypes_Documents_file, datatypes_Documents_tab_counter}

# datatypes_Json class attributes and methods
datatypes_Json_values: Property = Property(name="values", type=datatypes_Value)
datatypes_Json.attributes={datatypes_Json_values}

# datatypes_Number class attributes and methods
datatypes_Number_data: Property = Property(name="data", type=IntegerType)
datatypes_Number.attributes={datatypes_Number_data}

# datatypes_String class attributes and methods
datatypes_String_data: Property = Property(name="data", type=datatypes_String)
datatypes_String.attributes={datatypes_String_data}

# datatypes_Bool class attributes and methods
datatypes_Bool_data: Property = Property(name="data", type=BooleanType)
datatypes_Bool.attributes={datatypes_Bool_data}

# datatypes_Array class attributes and methods
datatypes_Array_data: Property = Property(name="data", type=datatypes_Value)
datatypes_Array.attributes={datatypes_Array_data}

# datatypes_Value class attributes and methods
datatypes_Value_attribute: Property = Property(name="attribute", type=StringType)
datatypes_Value.attributes={datatypes_Value_attribute}

# user_Business class attributes and methods
user_Business_id: Property = Property(name="id", type=datatypes_String)
user_Business_name: Property = Property(name="name", type=datatypes_String)
user_Business_category: Property = Property(name="category", type=StringType)
user_Business_website: Property = Property(name="website", type=StringType)
user_Business_email: Property = Property(name="email", type=StringType)
user_Business_phone: Property = Property(name="phone", type=StringType)
user_Business_address: Property = Property(name="address", type=Address)
user_Business_adminUser: Property = Property(name="adminUser", type=user_User)
user_Business_staffUsers: Property = Property(name="staffUsers", type=user_User)
user_Business_products: Property = Property(name="products", type=marketing_Product)
user_Business_avgRatings: Property = Property(name="avgRatings", type=datatypes_Number)
user_Business_tags: Property = Property(name="tags", type=user_Tags)
user_Business.attributes={user_Business_id, user_Business_address, user_Business_products, user_Business_avgRatings, user_Business_email, user_Business_phone, user_Business_name, user_Business_staffUsers, user_Business_website, user_Business_category, user_Business_tags, user_Business_adminUser}

# user_User class attributes and methods
user_User_id: Property = Property(name="id", type=datatypes_String)
user_User_fiirstName: Property = Property(name="fiirstName", type=datatypes_String)
user_User_lastName: Property = Property(name="lastName", type=datatypes_String)
user_User_email: Property = Property(name="email", type=StringType)
user_User_phone: Property = Property(name="phone", type=datatypes_String)
user_User_displayName: Property = Property(name="displayName", type=StringType)
user_User_photoURL: Property = Property(name="photoURL", type=StringType)
user_User_address: Property = Property(name="address", type=Address)
user_User_provider: Property = Property(name="provider", type=user_Provider)
user_User_interests: Property = Property(name="interests", type=system_Category)
user_User_wishlist: Property = Property(name="wishlist", type=marketing_Product)
user_User_purchaseHistory: Property = Property(name="purchaseHistory", type=marketing_Product)
user_User_reviews: Property = Property(name="reviews", type=marketing_Review)
user_User_business: Property = Property(name="business", type=user_Business)
user_User.attributes={user_User_reviews, user_User_purchaseHistory, user_User_photoURL, user_User_business, user_User_phone, user_User_interests, user_User_lastName, user_User_fiirstName, user_User_wishlist, user_User_address, user_User_provider, user_User_id, user_User_displayName, user_User_email}

# user_Provider class attributes and methods
user_Provider_providerId: Property = Property(name="providerId", type=StringType)
user_Provider_displayName: Property = Property(name="displayName", type=StringType)
user_Provider_email: Property = Property(name="email", type=StringType)
user_Provider_photoURL: Property = Property(name="photoURL", type=StringType)
user_Provider_uid: Property = Property(name="uid", type=StringType)
user_Provider.attributes={user_Provider_providerId, user_Provider_photoURL, user_Provider_email, user_Provider_displayName, user_Provider_uid}

# user_Tags class attributes and methods
user_Tags_id: Property = Property(name="id", type=StringType)
user_Tags_name: Property = Property(name="name", type=StringType)
user_Tags.attributes={user_Tags_id, user_Tags_name}

# marketing_Product class attributes and methods
marketing_Product_id: Property = Property(name="id", type=StringType)
marketing_Product_busId: Property = Property(name="busId", type=user_Business)
marketing_Product_name: Property = Property(name="name", type=StringType)
marketing_Product_ccategory: Property = Property(name="ccategory", type=system_Category)
marketing_Product_price: Property = Property(name="price", type=FloatType)
marketing_Product_active: Property = Property(name="active", type=BooleanType)
marketing_Product_created: Property = Property(name="created", type=DateType)
marketing_Product_expires: Property = Property(name="expires", type=DateType)
marketing_Product_reviews: Property = Property(name="reviews", type=marketing_Review)
marketing_Product.attributes={marketing_Product_active, marketing_Product_created, marketing_Product_name, marketing_Product_price, marketing_Product_busId, marketing_Product_ccategory, marketing_Product_expires, marketing_Product_id, marketing_Product_reviews}

# marketing_Review class attributes and methods
marketing_Review_id: Property = Property(name="id", type=StringType)
marketing_Review_product: Property = Property(name="product", type=marketing_Product)
marketing_Review_user: Property = Property(name="user", type=user_User)
marketing_Review_rating: Property = Property(name="rating", type=datatypes_Number)
marketing_Review_description: Property = Property(name="description", type=StringType)
marketing_Review.attributes={marketing_Review_rating, marketing_Review_id, marketing_Review_user, marketing_Review_description, marketing_Review_product}

# system_Category class attributes and methods
system_Category_id: Property = Property(name="id", type=StringType)
system_Category_section: Property = Property(name="section", type=StringType)
system_Category_name: Property = Property(name="name", type=StringType)
system_Category_parent: Property = Property(name="parent", type=system_Category)
system_Category_icon: Property = Property(name="icon", type=StringType)
system_Category.attributes={system_Category_icon, system_Category_name, system_Category_section, system_Category_parent, system_Category_id}

# Address class attributes and methods
Address_street: Property = Property(name="street", type=StringType)
Address_suburb: Property = Property(name="suburb", type=StringType)
Address_state: Property = Property(name="state", type=StringType)
Address_postcode: Property = Property(name="postcode", type=StringType)
Address_country: Property = Property(name="country", type=datatypes_String)
Address.attributes={Address_postcode, Address_street, Address_country, Address_state, Address_suburb}

# Domain Model
domain_model = DomainModel(
    name="_XI_1kAVJEeipbtix_oa2Dg",
    types={datatypes_Documents, datatypes_Json, datatypes_Number, datatypes_String, datatypes_Bool, datatypes_Array, datatypes_Value, user_Business, user_User, user_Provider, user_Tags, marketing_Product, marketing_Review, system_Category, Address},
    associations={},
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