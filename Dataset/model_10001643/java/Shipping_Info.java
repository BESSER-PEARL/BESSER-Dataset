





import java.util.List;
import java.util.ArrayList;

public class Shipping_Info  {

    private int Shipping_Id;
    private String Shipping_Type;





    private Orders orders;


    public Shipping_Info(
        int Shipping_Id,        String Shipping_Type    ) {
        this.Shipping_Id = Shipping_Id;
        this.Shipping_Type = Shipping_Type;
    }


    public int getShipping_id() {
        return Shipping_Id;
    }

    public void setShipping_id(int Shipping_Id) {
        this.Shipping_Id = Shipping_Id;
    }
    public String getShipping_type() {
        return Shipping_Type;
    }

    public void setShipping_type(String Shipping_Type) {
        this.Shipping_Type = Shipping_Type;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}