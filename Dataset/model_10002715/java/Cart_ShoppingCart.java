




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Cart_ShoppingCart  {

    private int id;
    private float GetTotal__;
    private int AddCart;
    private int UpdateOrder;
    private int RemoveOrder;
    private LocalDate creationDate;
    private int CheckoutID;





    private GUI_Screen gui_screen;




    private Customer_Customer1 customer_customer1;


    public Cart_ShoppingCart(
        int id,        float GetTotal__,        int AddCart,        int UpdateOrder,        int RemoveOrder,        LocalDate creationDate,        int CheckoutID    ) {
        this.id = id;
        this.GetTotal__ = GetTotal__;
        this.AddCart = AddCart;
        this.UpdateOrder = UpdateOrder;
        this.RemoveOrder = RemoveOrder;
        this.creationDate = creationDate;
        this.CheckoutID = CheckoutID;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getGettotal__() {
        return GetTotal__;
    }

    public void setGettotal__(float GetTotal__) {
        this.GetTotal__ = GetTotal__;
    }
    public int getAddcart() {
        return AddCart;
    }

    public void setAddcart(int AddCart) {
        this.AddCart = AddCart;
    }
    public int getUpdateorder() {
        return UpdateOrder;
    }

    public void setUpdateorder(int UpdateOrder) {
        this.UpdateOrder = UpdateOrder;
    }
    public int getRemoveorder() {
        return RemoveOrder;
    }

    public void setRemoveorder(int RemoveOrder) {
        this.RemoveOrder = RemoveOrder;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public int getCheckoutid() {
        return CheckoutID;
    }

    public void setCheckoutid(int CheckoutID) {
        this.CheckoutID = CheckoutID;
    }

    public GUI_Screen getGui_screen() {
        return gui_screen;
    }

    public void setGui_screen(GUI_Screen gui_screen) {
        this.gui_screen = gui_screen;
    }
    public Customer_Customer1 getCustomer_customer1() {
        return customer_customer1;
    }

    public void setCustomer_customer1(Customer_Customer1 customer_customer1) {
        this.customer_customer1 = customer_customer1;
    }

}