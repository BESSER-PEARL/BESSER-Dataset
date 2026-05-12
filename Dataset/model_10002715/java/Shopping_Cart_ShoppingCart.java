




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart_ShoppingCart  {

    private int id;
    private LocalDate creationDate;
    private int UpdateOrder;
    private int CheckoutID;
    private int AddOrder;
    private float GetTotal__;
    private int RemoveOrder;





    private Customer_Customer customer_customer;


    public Shopping_Cart_ShoppingCart(
        int id,        LocalDate creationDate,        int UpdateOrder,        int CheckoutID,        int AddOrder,        float GetTotal__,        int RemoveOrder    ) {
        this.id = id;
        this.creationDate = creationDate;
        this.UpdateOrder = UpdateOrder;
        this.CheckoutID = CheckoutID;
        this.AddOrder = AddOrder;
        this.GetTotal__ = GetTotal__;
        this.RemoveOrder = RemoveOrder;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public int getUpdateorder() {
        return UpdateOrder;
    }

    public void setUpdateorder(int UpdateOrder) {
        this.UpdateOrder = UpdateOrder;
    }
    public int getCheckoutid() {
        return CheckoutID;
    }

    public void setCheckoutid(int CheckoutID) {
        this.CheckoutID = CheckoutID;
    }
    public int getAddorder() {
        return AddOrder;
    }

    public void setAddorder(int AddOrder) {
        this.AddOrder = AddOrder;
    }
    public float getGettotal__() {
        return GetTotal__;
    }

    public void setGettotal__(float GetTotal__) {
        this.GetTotal__ = GetTotal__;
    }
    public int getRemoveorder() {
        return RemoveOrder;
    }

    public void setRemoveorder(int RemoveOrder) {
        this.RemoveOrder = RemoveOrder;
    }

    public Customer_Customer getCustomer_customer() {
        return customer_customer;
    }

    public void setCustomer_customer(Customer_Customer customer_customer) {
        this.customer_customer = customer_customer;
    }

}