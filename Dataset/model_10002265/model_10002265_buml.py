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
Customer = Class(name="Customer")
Payment = Class(name="Payment")
ConNguoi = Class(name="ConNguoi")
Account = Class(name="Account")
SinhVien = Class(name="SinhVien")
Order = Class(name="Order")
BoMon = Class(name="BoMon")
Khoa = Class(name="Khoa")

# Customer class attributes and methods
Customer_address: Property = Property(name="address", type=StringType)
Customer_phone: Property = Property(name="phone", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_phone, Customer_email, Customer_address}

# Payment class attributes and methods
Payment_paidDate: Property = Property(name="paidDate", type=DateType)
Payment_total: Property = Property(name="total", type=FloatType)
Payment_details: Property = Property(name="details", type=StringType)
Payment.attributes={Payment_paidDate, Payment_details, Payment_total}

# ConNguoi class attributes and methods
ConNguoi_CMND: Property = Property(name="CMND", type=StringType)
ConNguoi_hoten: Property = Property(name="hoten", type=StringType)
ConNguoi_ngaysinh: Property = Property(name="ngaysinh", type=DateType)
ConNguoi_gioitinh: Property = Property(name="gioitinh", type=BooleanType)
ConNguoi_diachi: Property = Property(name="diachi", type=StringType)
ConNguoi.attributes={ConNguoi_diachi, ConNguoi_ngaysinh, ConNguoi_hoten, ConNguoi_CMND, ConNguoi_gioitinh}

# Account class attributes and methods
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account_open: Property = Property(name="open", type=DateType)
Account_closed: Property = Property(name="closed", type=DateType)
Account_isClosed: Property = Property(name="isClosed", type=BooleanType)
Account.attributes={Account_billingAddress, Account_open, Account_isClosed, Account_closed}

# SinhVien class attributes and methods
SinhVien_MSSV: Property = Property(name="MSSV", type=StringType)
SinhVien_lop: Property = Property(name="lop", type=StringType)
SinhVien_nganhhoc: Property = Property(name="nganhhoc", type=StringType)
SinhVien_bomon: Property = Property(name="bomon", type=StringType)
SinhVien.attributes={SinhVien_MSSV, SinhVien_lop, SinhVien_nganhhoc, SinhVien_bomon}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=IntegerType)
Order_ordered: Property = Property(name="ordered", type=DateType)
Order_shipped: Property = Property(name="shipped", type=BooleanType)
Order_shipTo: Property = Property(name="shipTo", type=StringType)
Order_total: Property = Property(name="total", type=FloatType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_shipped, Order_total, Order_ordered, Order_number, Order_status, Order_shipTo}

# BoMon class attributes and methods
BoMon_mabomon: Property = Property(name="mabomon", type=StringType)
BoMon_tenbomon: Property = Property(name="tenbomon", type=StringType)
BoMon.attributes={BoMon_tenbomon, BoMon_mabomon}

# Khoa class attributes and methods
Khoa_makhoa: Property = Property(name="makhoa", type=StringType)
Khoa_tenkhoa: Property = Property(name="tenkhoa", type=StringType)
Khoa.attributes={Khoa_tenkhoa, Khoa_makhoa}

# Relationships
Account_Payment: BinaryAssociation = BinaryAssociation(
    name="Account_Payment",
    ends={
        Property(name="p0", type=Payment, multiplicity=Multiplicity(0, 9999)),
        Property(name="acc1", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser3", type=SinhVien, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart6", type=ConNguoi, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="co8", type=BoMon, multiplicity=Multiplicity(1, 9999)),
        Property(name="thus9", type=Khoa, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account11", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order12", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment13", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a11d8d4d_0d3e_44a0_bf4a_ab9b14c57e11",
    types={Customer, Payment, ConNguoi, Account, SinhVien, Order, BoMon, Khoa},
    associations={Account_Payment, WebUser_Customer, Customer_Account, Account_ShoppingCart, Product_LineItem, Account_Order, Payment_Order},
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