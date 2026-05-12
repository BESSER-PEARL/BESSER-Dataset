





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Delivertiony_Informa  {

    private None Receiver_Name;
    private None Other_Delivery_Address;
    private None Delivery_Address;
    private String Delivery_Phone;





    private online_shopping_Orders online_shopping_orders;


    public online_shopping_Delivertiony_Informa(
        None Receiver_Name,        None Other_Delivery_Address,        None Delivery_Address,        String Delivery_Phone    ) {
        this.Receiver_Name = Receiver_Name;
        this.Other_Delivery_Address = Other_Delivery_Address;
        this.Delivery_Address = Delivery_Address;
        this.Delivery_Phone = Delivery_Phone;
    }


    public None getReceiver_name() {
        return Receiver_Name;
    }

    public void setReceiver_name(None Receiver_Name) {
        this.Receiver_Name = Receiver_Name;
    }
    public None getOther_delivery_address() {
        return Other_Delivery_Address;
    }

    public void setOther_delivery_address(None Other_Delivery_Address) {
        this.Other_Delivery_Address = Other_Delivery_Address;
    }
    public None getDelivery_address() {
        return Delivery_Address;
    }

    public void setDelivery_address(None Delivery_Address) {
        this.Delivery_Address = Delivery_Address;
    }
    public String getDelivery_phone() {
        return Delivery_Phone;
    }

    public void setDelivery_phone(String Delivery_Phone) {
        this.Delivery_Phone = Delivery_Phone;
    }

    public online_shopping_Orders getOnline_shopping_orders() {
        return online_shopping_orders;
    }

    public void setOnline_shopping_orders(online_shopping_Orders online_shopping_orders) {
        this.online_shopping_orders = online_shopping_orders;
    }

}