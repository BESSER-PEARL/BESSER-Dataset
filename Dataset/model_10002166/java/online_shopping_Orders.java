





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Orders  {

    private None Datw_Shipping;
    private None Customer_Name;
    private int Order_ID;
    private None Customer_ID;
    private None Date_Created;



    public online_shopping_Orders(
        None Datw_Shipping,        None Customer_Name,        int Order_ID,        None Customer_ID,        None Date_Created    ) {
        this.Datw_Shipping = Datw_Shipping;
        this.Customer_Name = Customer_Name;
        this.Order_ID = Order_ID;
        this.Customer_ID = Customer_ID;
        this.Date_Created = Date_Created;
    }


    public None getDatw_shipping() {
        return Datw_Shipping;
    }

    public void setDatw_shipping(None Datw_Shipping) {
        this.Datw_Shipping = Datw_Shipping;
    }
    public None getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(None Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public int getOrder_id() {
        return Order_ID;
    }

    public void setOrder_id(int Order_ID) {
        this.Order_ID = Order_ID;
    }
    public None getCustomer_id() {
        return Customer_ID;
    }

    public void setCustomer_id(None Customer_ID) {
        this.Customer_ID = Customer_ID;
    }
    public None getDate_created() {
        return Date_Created;
    }

    public void setDate_created(None Date_Created) {
        this.Date_Created = Date_Created;
    }


}