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
User = Class(name="User")
Admin = Class(name="Admin")
pembeli = Class(name="pembeli")
Cart = Class(name="Cart")
Order = Class(name="Order")
Orderdetail = Class(name="Orderdetail")
Shippinginfo = Class(name="Shippinginfo")
Produk = Class(name="Produk")
Kategori = Class(name="Kategori")
penjual = Class(name="penjual")
barang = Class(name="barang")
kategori = Class(name="kategori")
user = Class(name="user")
vendor = Class(name="vendor")
pembeli1 = Class(name="pembeli1")
role = Class(name="role")
order = Class(name="order")
orderdetail = Class(name="orderdetail")
admin = Class(name="admin")

# User class attributes and methods
User_id: Property = Property(name="id", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_id, User_password}

# Admin class attributes and methods
Admin_name: Property = Property(name="name", type=StringType)
Admin_mail: Property = Property(name="mail", type=StringType)
Admin.attributes={Admin_name, Admin_mail}

# pembeli class attributes and methods
pembeli_id: Property = Property(name="id", type=StringType)
pembeli_name: Property = Property(name="name", type=StringType)
pembeli_address: Property = Property(name="address", type=StringType)
pembeli_mail: Property = Property(name="mail", type=StringType)
pembeli_username: Property = Property(name="username", type=StringType)
pembeli_password: Property = Property(name="password", type=StringType)
pembeli_shippinginfo: Property = Property(name="shippinginfo", type=StringType)
pembeli.attributes={pembeli_id, pembeli_password, pembeli_username, pembeli_mail, pembeli_address, pembeli_shippinginfo, pembeli_name}

# Cart class attributes and methods
Cart_cartid: Property = Property(name="cartid", type=StringType)
Cart_productid: Property = Property(name="productid", type=StringType)
Cart_quantity: Property = Property(name="quantity", type=StringType)
Cart_date: Property = Property(name="date", type=StringType)
Cart.attributes={Cart_date, Cart_productid, Cart_cartid, Cart_quantity}

# Order class attributes and methods
Order_orderid: Property = Property(name="orderid", type=StringType)
Order_shippingid: Property = Property(name="shippingid", type=StringType)
Order_customerid: Property = Property(name="customerid", type=StringType)
Order_dateorder: Property = Property(name="dateorder", type=StringType)
Order_datedeliver: Property = Property(name="datedeliver", type=StringType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_datedeliver, Order_shippingid, Order_dateorder, Order_customerid, Order_orderid, Order_status}

# Orderdetail class attributes and methods
Orderdetail_orderid: Property = Property(name="orderid", type=StringType)
Orderdetail_productid: Property = Property(name="productid", type=StringType)
Orderdetail_quantity: Property = Property(name="quantity", type=StringType)
Orderdetail_cost: Property = Property(name="cost", type=StringType)
Orderdetail_total: Property = Property(name="total", type=StringType)
Orderdetail.attributes={Orderdetail_cost, Orderdetail_productid, Orderdetail_total, Orderdetail_orderid, Orderdetail_quantity}

# Shippinginfo class attributes and methods
Shippinginfo_shippingid: Property = Property(name="shippingid", type=StringType)
Shippinginfo_type: Property = Property(name="type", type=StringType)
Shippinginfo_cost: Property = Property(name="cost", type=StringType)
Shippinginfo_region: Property = Property(name="region", type=StringType)
Shippinginfo_total: Property = Property(name="total", type=StringType)
Shippinginfo.attributes={Shippinginfo_cost, Shippinginfo_shippingid, Shippinginfo_type, Shippinginfo_total, Shippinginfo_region}

# Produk class attributes and methods
Produk_productid: Property = Property(name="productid", type=StringType)
Produk_idkategori: Property = Property(name="idkategori", type=StringType)
Produk_name: Property = Property(name="name", type=StringType)
Produk_desc: Property = Property(name="desc", type=StringType)
Produk_price: Property = Property(name="price", type=StringType)
Produk.attributes={Produk_price, Produk_desc, Produk_name, Produk_productid, Produk_idkategori}

# Kategori class attributes and methods
Kategori_idkategori: Property = Property(name="idkategori", type=StringType)
Kategori_productid: Property = Property(name="productid", type=StringType)
Kategori_name: Property = Property(name="name", type=StringType)
Kategori_desc: Property = Property(name="desc", type=StringType)
Kategori.attributes={Kategori_name, Kategori_desc, Kategori_idkategori, Kategori_productid}

# penjual class attributes and methods
penjual_id: Property = Property(name="id", type=StringType)
penjual_name: Property = Property(name="name", type=StringType)
penjual_address: Property = Property(name="address", type=StringType)
penjual_mail: Property = Property(name="mail", type=StringType)
penjual_username: Property = Property(name="username", type=StringType)
penjual_password: Property = Property(name="password", type=StringType)
penjual_shippinginfo: Property = Property(name="shippinginfo", type=StringType)
penjual_bussinessname: Property = Property(name="bussinessname", type=StringType)
penjual_bank: Property = Property(name="bank", type=StringType)
penjual.attributes={penjual_mail, penjual_address, penjual_shippinginfo, penjual_bank, penjual_username, penjual_bussinessname, penjual_name, penjual_id, penjual_password}

# barang class attributes and methods
barang_id: Property = Property(name="id", type=IntegerType)
barang_id_kategori: Property = Property(name="id_kategori", type=IntegerType)
barang_nama_barang: Property = Property(name="nama_barang", type=StringType)
barang_deskripsi_barang: Property = Property(name="deskripsi_barang", type=StringType)
barang_harga_barang: Property = Property(name="harga_barang", type=IntegerType)
barang.attributes={barang_id, barang_id_kategori, barang_deskripsi_barang, barang_harga_barang, barang_nama_barang}

# kategori class attributes and methods
kategori_id: Property = Property(name="id", type=IntegerType)
kategori_nama_kategori: Property = Property(name="nama_kategori", type=StringType)
kategori_deskripsi_kategori: Property = Property(name="deskripsi_kategori", type=StringType)
kategori.attributes={kategori_id, kategori_nama_kategori, kategori_deskripsi_kategori}

# user class attributes and methods
user_id_user: Property = Property(name="id_user", type=IntegerType)
user_id_role: Property = Property(name="id_role", type=IntegerType)
user_id_order: Property = Property(name="id_order", type=IntegerType)
user.attributes={user_id_role, user_id_order, user_id_user}

# vendor class attributes and methods
vendor_id: Property = Property(name="id", type=IntegerType)
vendor_id_role: Property = Property(name="id_role", type=IntegerType)
vendor_name: Property = Property(name="name", type=StringType)
vendor_address: Property = Property(name="address", type=StringType)
vendor_mail: Property = Property(name="mail", type=StringType)
vendor_username: Property = Property(name="username", type=StringType)
vendor_password: Property = Property(name="password", type=StringType)
vendor_shippinginfo: Property = Property(name="shippinginfo", type=StringType)
vendor_bussinessname: Property = Property(name="bussinessname", type=StringType)
vendor_bank: Property = Property(name="bank", type=StringType)
vendor.attributes={vendor_password, vendor_shippinginfo, vendor_name, vendor_id_role, vendor_username, vendor_bank, vendor_id, vendor_address, vendor_mail, vendor_bussinessname}

# pembeli1 class attributes and methods
pembeli1_id: Property = Property(name="id", type=IntegerType)
pembeli1_id_role: Property = Property(name="id_role", type=IntegerType)
pembeli1_name: Property = Property(name="name", type=StringType)
pembeli1_address: Property = Property(name="address", type=StringType)
pembeli1_mail: Property = Property(name="mail", type=StringType)
pembeli1_username: Property = Property(name="username", type=StringType)
pembeli1_password: Property = Property(name="password", type=StringType)
pembeli1.attributes={pembeli1_password, pembeli1_name, pembeli1_id, pembeli1_id_role, pembeli1_mail, pembeli1_address, pembeli1_username}

# role class attributes and methods
role_id: Property = Property(name="id", type=IntegerType)
role_nama_role: Property = Property(name="nama_role", type=StringType)
role_deskripsi_role: Property = Property(name="deskripsi_role", type=StringType)
role.attributes={role_id, role_nama_role, role_deskripsi_role}

# order class attributes and methods
order_order_id: Property = Property(name="order_id", type=IntegerType)
order_id_user: Property = Property(name="id_user", type=IntegerType)
order_dateorder: Property = Property(name="dateorder", type=StringType)
order_status: Property = Property(name="status", type=StringType)
order.attributes={order_status, order_id_user, order_order_id, order_dateorder}

# orderdetail class attributes and methods
orderdetail_order_id: Property = Property(name="order_id", type=IntegerType)
orderdetail_barang_id: Property = Property(name="barang_id", type=IntegerType)
orderdetail_total: Property = Property(name="total", type=StringType)
orderdetail.attributes={orderdetail_order_id, orderdetail_barang_id, orderdetail_total}

# admin class attributes and methods
admin_id: Property = Property(name="id", type=IntegerType)
admin_username: Property = Property(name="username", type=StringType)
admin_password: Property = Property(name="password", type=StringType)
admin.attributes={admin_password, admin_id, admin_username}

# Relationships
Shippinginfo_Order: BinaryAssociation = BinaryAssociation(
    name="Shippinginfo_Order",
    ends={
        Property(name="order0", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="shippinginfo1", type=Shippinginfo, multiplicity=Multiplicity(0, 1))
    }
)
Orderdetail_Order: BinaryAssociation = BinaryAssociation(
    name="Orderdetail_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="orderdetail3", type=Orderdetail, multiplicity=Multiplicity(0, 1))
    }
)
Cart_Customer: BinaryAssociation = BinaryAssociation(
    name="Cart_Customer",
    ends={
        Property(name="customer4", type=pembeli, multiplicity=Multiplicity(0, 1)),
        Property(name="cart5", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)
penjual_User: BinaryAssociation = BinaryAssociation(
    name="penjual_User",
    ends={
        Property(name="user6", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="penjual7", type=penjual, multiplicity=Multiplicity(0, 1))
    }
)
Produk_Orderdetail: BinaryAssociation = BinaryAssociation(
    name="Produk_Orderdetail",
    ends={
        Property(name="orderdetail8", type=Orderdetail, multiplicity=Multiplicity(1, 1)),
        Property(name="produk9", type=Produk, multiplicity=Multiplicity(0, 9999))
    }
)
Produk_Kategori: BinaryAssociation = BinaryAssociation(
    name="Produk_Kategori",
    ends={
        Property(name="kategori10", type=Kategori, multiplicity=Multiplicity(1, 1)),
        Property(name="produk11", type=Produk, multiplicity=Multiplicity(1, 1))
    }
)
role_user: BinaryAssociation = BinaryAssociation(
    name="role_user",
    ends={
        Property(name="user12", type=user, multiplicity=Multiplicity(1, 1)),
        Property(name="role13", type=role, multiplicity=Multiplicity(1, 1))
    }
)
admin_user: BinaryAssociation = BinaryAssociation(
    name="admin_user",
    ends={
        Property(name="user14", type=user, multiplicity=Multiplicity(1, 1)),
        Property(name="admin15", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
pembeli_user: BinaryAssociation = BinaryAssociation(
    name="pembeli_user",
    ends={
        Property(name="user16", type=user, multiplicity=Multiplicity(1, 1)),
        Property(name="pembeli17", type=pembeli1, multiplicity=Multiplicity(1, 1))
    }
)
vendor_user: BinaryAssociation = BinaryAssociation(
    name="vendor_user",
    ends={
        Property(name="user18", type=user, multiplicity=Multiplicity(1, 1)),
        Property(name="vendor19", type=vendor, multiplicity=Multiplicity(1, 1))
    }
)
order_user: BinaryAssociation = BinaryAssociation(
    name="order_user",
    ends={
        Property(name="user20", type=user, multiplicity=Multiplicity(1, 1)),
        Property(name="order21", type=order, multiplicity=Multiplicity(0, 9999))
    }
)
order_orderdetail: BinaryAssociation = BinaryAssociation(
    name="order_orderdetail",
    ends={
        Property(name="orderdetail22", type=orderdetail, multiplicity=Multiplicity(0, 1)),
        Property(name="order23", type=order, multiplicity=Multiplicity(0, 1))
    }
)
barang_kategori: BinaryAssociation = BinaryAssociation(
    name="barang_kategori",
    ends={
        Property(name="kategori24", type=kategori, multiplicity=Multiplicity(1, 1)),
        Property(name="barang25", type=barang, multiplicity=Multiplicity(1, 1))
    }
)
orderdetail_barang: BinaryAssociation = BinaryAssociation(
    name="orderdetail_barang",
    ends={
        Property(name="barang26", type=barang, multiplicity=Multiplicity(0, 9999)),
        Property(name="orderdetail27", type=orderdetail, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_369f8d51_0c87_47c2_8b96_fb435ee860c1",
    types={User, Admin, pembeli, Cart, Order, Orderdetail, Shippinginfo, Produk, Kategori, penjual, barang, kategori, user, vendor, pembeli1, role, order, orderdetail, admin},
    associations={Shippinginfo_Order, Orderdetail_Order, Cart_Customer, penjual_User, Produk_Orderdetail, Produk_Kategori, role_user, admin_user, pembeli_user, vendor_user, order_user, order_orderdetail, barang_kategori, orderdetail_barang},
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