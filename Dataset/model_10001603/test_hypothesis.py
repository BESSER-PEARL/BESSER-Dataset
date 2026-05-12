import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Order,
    Chef,
    Food_Items,
    Food_Sub_Category,
    Customer,
    Food_Category,
    Table,
    Material,
    Food,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Order_status" in params, "Missing parameter 'Order_status'"
    assert "Order_id" in params, "Missing parameter 'Order_id'"
    assert "Order_delete" in params, "Missing parameter 'Order_delete'"
    assert "Order_num" in params, "Missing parameter 'Order_num'"
    assert "Order_edit" in params, "Missing parameter 'Order_edit'"

def test_order_has_Order_status():
    assert hasattr(Order, "Order_status")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_status" in klass.__dict__:
            descriptor = klass.__dict__["Order_status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Order_id():
    assert hasattr(Order, "Order_id")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_id" in klass.__dict__:
            descriptor = klass.__dict__["Order_id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Order_delete():
    assert hasattr(Order, "Order_delete")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_delete" in klass.__dict__:
            descriptor = klass.__dict__["Order_delete"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Order_num():
    assert hasattr(Order, "Order_num")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_num" in klass.__dict__:
            descriptor = klass.__dict__["Order_num"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Order_edit():
    assert hasattr(Order, "Order_edit")
    descriptor = None
    for klass in Order.__mro__:
        if "Order_edit" in klass.__dict__:
            descriptor = klass.__dict__["Order_edit"]
            break
    assert isinstance(descriptor, property)



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Speciality" in params, "Missing parameter 'Speciality'"
    assert "Chef_name" in params, "Missing parameter 'Chef_name'"
    assert "Chef_id" in params, "Missing parameter 'Chef_id'"

def test_chef_has_order_id():
    assert hasattr(Chef, "order_id")
    descriptor = None
    for klass in Chef.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_Status():
    assert hasattr(Chef, "Status")
    descriptor = None
    for klass in Chef.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_Speciality():
    assert hasattr(Chef, "Speciality")
    descriptor = None
    for klass in Chef.__mro__:
        if "Speciality" in klass.__dict__:
            descriptor = klass.__dict__["Speciality"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_Chef_name():
    assert hasattr(Chef, "Chef_name")
    descriptor = None
    for klass in Chef.__mro__:
        if "Chef_name" in klass.__dict__:
            descriptor = klass.__dict__["Chef_name"]
            break
    assert isinstance(descriptor, property)

def test_chef_has_Chef_id():
    assert hasattr(Chef, "Chef_id")
    descriptor = None
    for klass in Chef.__mro__:
        if "Chef_id" in klass.__dict__:
            descriptor = klass.__dict__["Chef_id"]
            break
    assert isinstance(descriptor, property)



def test_food_items_is_not_abstract():
    assert not inspect.isabstract(Food_Items)


def test_food_items_constructor_exists():
    assert callable(Food_Items.__init__)


def test_food_items_constructor_args():
    sig = inspect.signature(Food_Items.__init__)
    params = list(sig.parameters.keys())
    assert "Food_id" in params, "Missing parameter 'Food_id'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "Items_id" in params, "Missing parameter 'Items_id'"
    assert "Material_id" in params, "Missing parameter 'Material_id'"

def test_food_items_has_Food_id():
    assert hasattr(Food_Items, "Food_id")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Food_id" in klass.__dict__:
            descriptor = klass.__dict__["Food_id"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_quantity():
    assert hasattr(Food_Items, "quantity")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_Items_id():
    assert hasattr(Food_Items, "Items_id")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Items_id" in klass.__dict__:
            descriptor = klass.__dict__["Items_id"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_Material_id():
    assert hasattr(Food_Items, "Material_id")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Material_id" in klass.__dict__:
            descriptor = klass.__dict__["Material_id"]
            break
    assert isinstance(descriptor, property)



def test_food_sub_category_is_not_abstract():
    assert not inspect.isabstract(Food_Sub_Category)


def test_food_sub_category_constructor_exists():
    assert callable(Food_Sub_Category.__init__)


def test_food_sub_category_constructor_args():
    sig = inspect.signature(Food_Sub_Category.__init__)
    params = list(sig.parameters.keys())
    assert "sub_descp" in params, "Missing parameter 'sub_descp'"
    assert "sub_id" in params, "Missing parameter 'sub_id'"
    assert "sub_image" in params, "Missing parameter 'sub_image'"
    assert "sub_name" in params, "Missing parameter 'sub_name'"

def test_food_sub_category_has_sub_descp():
    assert hasattr(Food_Sub_Category, "sub_descp")
    descriptor = None
    for klass in Food_Sub_Category.__mro__:
        if "sub_descp" in klass.__dict__:
            descriptor = klass.__dict__["sub_descp"]
            break
    assert isinstance(descriptor, property)

def test_food_sub_category_has_sub_id():
    assert hasattr(Food_Sub_Category, "sub_id")
    descriptor = None
    for klass in Food_Sub_Category.__mro__:
        if "sub_id" in klass.__dict__:
            descriptor = klass.__dict__["sub_id"]
            break
    assert isinstance(descriptor, property)

def test_food_sub_category_has_sub_image():
    assert hasattr(Food_Sub_Category, "sub_image")
    descriptor = None
    for klass in Food_Sub_Category.__mro__:
        if "sub_image" in klass.__dict__:
            descriptor = klass.__dict__["sub_image"]
            break
    assert isinstance(descriptor, property)

def test_food_sub_category_has_sub_name():
    assert hasattr(Food_Sub_Category, "sub_name")
    descriptor = None
    for klass in Food_Sub_Category.__mro__:
        if "sub_name" in klass.__dict__:
            descriptor = klass.__dict__["sub_name"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "TimeStamp" in params, "Missing parameter 'TimeStamp'"
    assert "Table_id" in params, "Missing parameter 'Table_id'"
    assert "Customer_name" in params, "Missing parameter 'Customer_name'"
    assert "Customer_id" in params, "Missing parameter 'Customer_id'"
    assert "Status" in params, "Missing parameter 'Status'"

def test_customer_has_TimeStamp():
    assert hasattr(Customer, "TimeStamp")
    descriptor = None
    for klass in Customer.__mro__:
        if "TimeStamp" in klass.__dict__:
            descriptor = klass.__dict__["TimeStamp"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Table_id():
    assert hasattr(Customer, "Table_id")
    descriptor = None
    for klass in Customer.__mro__:
        if "Table_id" in klass.__dict__:
            descriptor = klass.__dict__["Table_id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Customer_name():
    assert hasattr(Customer, "Customer_name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Customer_name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Customer_id():
    assert hasattr(Customer, "Customer_id")
    descriptor = None
    for klass in Customer.__mro__:
        if "Customer_id" in klass.__dict__:
            descriptor = klass.__dict__["Customer_id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Status():
    assert hasattr(Customer, "Status")
    descriptor = None
    for klass in Customer.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)



def test_food_category_is_not_abstract():
    assert not inspect.isabstract(Food_Category)


def test_food_category_constructor_exists():
    assert callable(Food_Category.__init__)


def test_food_category_constructor_args():
    sig = inspect.signature(Food_Category.__init__)
    params = list(sig.parameters.keys())
    assert "Category_image" in params, "Missing parameter 'Category_image'"
    assert "Category_id" in params, "Missing parameter 'Category_id'"
    assert "sub_id" in params, "Missing parameter 'sub_id'"
    assert "Category_descp" in params, "Missing parameter 'Category_descp'"
    assert "Category_name" in params, "Missing parameter 'Category_name'"

def test_food_category_has_Category_image():
    assert hasattr(Food_Category, "Category_image")
    descriptor = None
    for klass in Food_Category.__mro__:
        if "Category_image" in klass.__dict__:
            descriptor = klass.__dict__["Category_image"]
            break
    assert isinstance(descriptor, property)

def test_food_category_has_Category_id():
    assert hasattr(Food_Category, "Category_id")
    descriptor = None
    for klass in Food_Category.__mro__:
        if "Category_id" in klass.__dict__:
            descriptor = klass.__dict__["Category_id"]
            break
    assert isinstance(descriptor, property)

def test_food_category_has_sub_id():
    assert hasattr(Food_Category, "sub_id")
    descriptor = None
    for klass in Food_Category.__mro__:
        if "sub_id" in klass.__dict__:
            descriptor = klass.__dict__["sub_id"]
            break
    assert isinstance(descriptor, property)

def test_food_category_has_Category_descp():
    assert hasattr(Food_Category, "Category_descp")
    descriptor = None
    for klass in Food_Category.__mro__:
        if "Category_descp" in klass.__dict__:
            descriptor = klass.__dict__["Category_descp"]
            break
    assert isinstance(descriptor, property)

def test_food_category_has_Category_name():
    assert hasattr(Food_Category, "Category_name")
    descriptor = None
    for klass in Food_Category.__mro__:
        if "Category_name" in klass.__dict__:
            descriptor = klass.__dict__["Category_name"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Table_id" in params, "Missing parameter 'Table_id'"
    assert "Table_num" in params, "Missing parameter 'Table_num'"

def test_table_has_Status():
    assert hasattr(Table, "Status")
    descriptor = None
    for klass in Table.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_table_has_Table_id():
    assert hasattr(Table, "Table_id")
    descriptor = None
    for klass in Table.__mro__:
        if "Table_id" in klass.__dict__:
            descriptor = klass.__dict__["Table_id"]
            break
    assert isinstance(descriptor, property)

def test_table_has_Table_num():
    assert hasattr(Table, "Table_num")
    descriptor = None
    for klass in Table.__mro__:
        if "Table_num" in klass.__dict__:
            descriptor = klass.__dict__["Table_num"]
            break
    assert isinstance(descriptor, property)



def test_material_is_not_abstract():
    assert not inspect.isabstract(Material)


def test_material_constructor_exists():
    assert callable(Material.__init__)


def test_material_constructor_args():
    sig = inspect.signature(Material.__init__)
    params = list(sig.parameters.keys())
    assert "Stock1" in params, "Missing parameter 'Stock1'"
    assert "Unit" in params, "Missing parameter 'Unit'"
    assert "Stock" in params, "Missing parameter 'Stock'"
    assert "Material_name" in params, "Missing parameter 'Material_name'"
    assert "Material_id" in params, "Missing parameter 'Material_id'"

def test_material_has_Stock1():
    assert hasattr(Material, "Stock1")
    descriptor = None
    for klass in Material.__mro__:
        if "Stock1" in klass.__dict__:
            descriptor = klass.__dict__["Stock1"]
            break
    assert isinstance(descriptor, property)

def test_material_has_Unit():
    assert hasattr(Material, "Unit")
    descriptor = None
    for klass in Material.__mro__:
        if "Unit" in klass.__dict__:
            descriptor = klass.__dict__["Unit"]
            break
    assert isinstance(descriptor, property)

def test_material_has_Stock():
    assert hasattr(Material, "Stock")
    descriptor = None
    for klass in Material.__mro__:
        if "Stock" in klass.__dict__:
            descriptor = klass.__dict__["Stock"]
            break
    assert isinstance(descriptor, property)

def test_material_has_Material_name():
    assert hasattr(Material, "Material_name")
    descriptor = None
    for klass in Material.__mro__:
        if "Material_name" in klass.__dict__:
            descriptor = klass.__dict__["Material_name"]
            break
    assert isinstance(descriptor, property)

def test_material_has_Material_id():
    assert hasattr(Material, "Material_id")
    descriptor = None
    for klass in Material.__mro__:
        if "Material_id" in klass.__dict__:
            descriptor = klass.__dict__["Material_id"]
            break
    assert isinstance(descriptor, property)



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "Category_id" in params, "Missing parameter 'Category_id'"
    assert "food_name" in params, "Missing parameter 'food_name'"

def test_food_has_food_id():
    assert hasattr(Food, "food_id")
    descriptor = None
    for klass in Food.__mro__:
        if "food_id" in klass.__dict__:
            descriptor = klass.__dict__["food_id"]
            break
    assert isinstance(descriptor, property)

def test_food_has_Category_id():
    assert hasattr(Food, "Category_id")
    descriptor = None
    for klass in Food.__mro__:
        if "Category_id" in klass.__dict__:
            descriptor = klass.__dict__["Category_id"]
            break
    assert isinstance(descriptor, property)

def test_food_has_food_name():
    assert hasattr(Food, "food_name")
    descriptor = None
    for klass in Food.__mro__:
        if "food_name" in klass.__dict__:
            descriptor = klass.__dict__["food_name"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Order_strategy = st.builds(
    Order,
    Order_status=
        safe_text,
    Order_id=
        st.integers(),
    Order_delete=
        safe_text,
    Order_num=
        st.integers(),
    Order_edit=
        safe_text
)
Chef_strategy = st.builds(
    Chef,
    order_id=
        st.integers(),
    Status=
        safe_text,
    Speciality=
        safe_text,
    Chef_name=
        safe_text,
    Chef_id=
        st.integers()
)
Food_Items_strategy = st.builds(
    Food_Items,
    Food_id=
        st.integers(),
    quantity=
        st.integers(),
    Items_id=
        st.integers(),
    Material_id=
        st.integers()
)
Food_Sub_Category_strategy = st.builds(
    Food_Sub_Category,
    sub_descp=
        safe_text,
    sub_id=
        st.integers(),
    sub_image=
        safe_text,
    sub_name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    TimeStamp=
        safe_text,
    Table_id=
        st.integers(),
    Customer_name=
        safe_text,
    Customer_id=
        st.integers(),
    Status=
        safe_text
)
Food_Category_strategy = st.builds(
    Food_Category,
    Category_image=
        safe_text,
    Category_id=
        st.integers(),
    sub_id=
        st.integers(),
    Category_descp=
        safe_text,
    Category_name=
        safe_text
)
Table_strategy = st.builds(
    Table,
    Status=
        safe_text,
    Table_id=
        st.integers(),
    Table_num=
        st.integers()
)
Material_strategy = st.builds(
    Material,
    Stock1=
        safe_text,
    Unit=
        safe_text,
    Stock=
        safe_text,
    Material_name=
        safe_text,
    Material_id=
        st.integers()
)
Food_strategy = st.builds(
    Food,
    food_id=
        st.integers(),
    Category_id=
        st.integers(),
    food_name=
        safe_text
)

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Order_status_setter(instance):
    original = instance.Order_status
    instance.Order_status = original
    assert instance.Order_status == original



@given(instance=Order_strategy)
def test_order_Order_id_setter(instance):
    original = instance.Order_id
    instance.Order_id = original
    assert instance.Order_id == original



@given(instance=Order_strategy)
def test_order_Order_delete_setter(instance):
    original = instance.Order_delete
    instance.Order_delete = original
    assert instance.Order_delete == original



@given(instance=Order_strategy)
def test_order_Order_num_setter(instance):
    original = instance.Order_num
    instance.Order_num = original
    assert instance.Order_num == original



@given(instance=Order_strategy)
def test_order_Order_edit_setter(instance):
    original = instance.Order_edit
    instance.Order_edit = original
    assert instance.Order_edit == original

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)



@given(instance=Chef_strategy)
def test_chef_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Chef_strategy)
def test_chef_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Chef_strategy)
def test_chef_Speciality_setter(instance):
    original = instance.Speciality
    instance.Speciality = original
    assert instance.Speciality == original



@given(instance=Chef_strategy)
def test_chef_Chef_name_setter(instance):
    original = instance.Chef_name
    instance.Chef_name = original
    assert instance.Chef_name == original



@given(instance=Chef_strategy)
def test_chef_Chef_id_setter(instance):
    original = instance.Chef_id
    instance.Chef_id = original
    assert instance.Chef_id == original

@given(instance=Food_Items_strategy)
@settings(max_examples=50)
def test_food_items_instantiation(instance):
    assert isinstance(instance, Food_Items)



@given(instance=Food_Items_strategy)
def test_food_items_Food_id_setter(instance):
    original = instance.Food_id
    instance.Food_id = original
    assert instance.Food_id == original



@given(instance=Food_Items_strategy)
def test_food_items_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Food_Items_strategy)
def test_food_items_Items_id_setter(instance):
    original = instance.Items_id
    instance.Items_id = original
    assert instance.Items_id == original



@given(instance=Food_Items_strategy)
def test_food_items_Material_id_setter(instance):
    original = instance.Material_id
    instance.Material_id = original
    assert instance.Material_id == original

@given(instance=Food_Sub_Category_strategy)
@settings(max_examples=50)
def test_food_sub_category_instantiation(instance):
    assert isinstance(instance, Food_Sub_Category)



@given(instance=Food_Sub_Category_strategy)
def test_food_sub_category_sub_descp_setter(instance):
    original = instance.sub_descp
    instance.sub_descp = original
    assert instance.sub_descp == original



@given(instance=Food_Sub_Category_strategy)
def test_food_sub_category_sub_id_setter(instance):
    original = instance.sub_id
    instance.sub_id = original
    assert instance.sub_id == original



@given(instance=Food_Sub_Category_strategy)
def test_food_sub_category_sub_image_setter(instance):
    original = instance.sub_image
    instance.sub_image = original
    assert instance.sub_image == original



@given(instance=Food_Sub_Category_strategy)
def test_food_sub_category_sub_name_setter(instance):
    original = instance.sub_name
    instance.sub_name = original
    assert instance.sub_name == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_TimeStamp_setter(instance):
    original = instance.TimeStamp
    instance.TimeStamp = original
    assert instance.TimeStamp == original



@given(instance=Customer_strategy)
def test_customer_Table_id_setter(instance):
    original = instance.Table_id
    instance.Table_id = original
    assert instance.Table_id == original



@given(instance=Customer_strategy)
def test_customer_Customer_name_setter(instance):
    original = instance.Customer_name
    instance.Customer_name = original
    assert instance.Customer_name == original



@given(instance=Customer_strategy)
def test_customer_Customer_id_setter(instance):
    original = instance.Customer_id
    instance.Customer_id = original
    assert instance.Customer_id == original



@given(instance=Customer_strategy)
def test_customer_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original

@given(instance=Food_Category_strategy)
@settings(max_examples=50)
def test_food_category_instantiation(instance):
    assert isinstance(instance, Food_Category)



@given(instance=Food_Category_strategy)
def test_food_category_Category_image_setter(instance):
    original = instance.Category_image
    instance.Category_image = original
    assert instance.Category_image == original



@given(instance=Food_Category_strategy)
def test_food_category_Category_id_setter(instance):
    original = instance.Category_id
    instance.Category_id = original
    assert instance.Category_id == original



@given(instance=Food_Category_strategy)
def test_food_category_sub_id_setter(instance):
    original = instance.sub_id
    instance.sub_id = original
    assert instance.sub_id == original



@given(instance=Food_Category_strategy)
def test_food_category_Category_descp_setter(instance):
    original = instance.Category_descp
    instance.Category_descp = original
    assert instance.Category_descp == original



@given(instance=Food_Category_strategy)
def test_food_category_Category_name_setter(instance):
    original = instance.Category_name
    instance.Category_name = original
    assert instance.Category_name == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Table_strategy)
def test_table_Table_id_setter(instance):
    original = instance.Table_id
    instance.Table_id = original
    assert instance.Table_id == original



@given(instance=Table_strategy)
def test_table_Table_num_setter(instance):
    original = instance.Table_num
    instance.Table_num = original
    assert instance.Table_num == original

@given(instance=Material_strategy)
@settings(max_examples=50)
def test_material_instantiation(instance):
    assert isinstance(instance, Material)



@given(instance=Material_strategy)
def test_material_Stock1_setter(instance):
    original = instance.Stock1
    instance.Stock1 = original
    assert instance.Stock1 == original



@given(instance=Material_strategy)
def test_material_Unit_setter(instance):
    original = instance.Unit
    instance.Unit = original
    assert instance.Unit == original



@given(instance=Material_strategy)
def test_material_Stock_setter(instance):
    original = instance.Stock
    instance.Stock = original
    assert instance.Stock == original



@given(instance=Material_strategy)
def test_material_Material_name_setter(instance):
    original = instance.Material_name
    instance.Material_name = original
    assert instance.Material_name == original



@given(instance=Material_strategy)
def test_material_Material_id_setter(instance):
    original = instance.Material_id
    instance.Material_id = original
    assert instance.Material_id == original

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)



@given(instance=Food_strategy)
def test_food_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Food_strategy)
def test_food_Category_id_setter(instance):
    original = instance.Category_id
    instance.Category_id = original
    assert instance.Category_id == original



@given(instance=Food_strategy)
def test_food_food_name_setter(instance):
    original = instance.food_name
    instance.food_name = original
    assert instance.food_name == original
