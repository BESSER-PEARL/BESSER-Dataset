





import java.util.List;
import java.util.ArrayList;

public class Shipping_Info  {

    private String Shipping_Type;
    private int Shipping_Id;





    private Orders orders;


    public Shipping_Info(
        String Shipping_Type,        int Shipping_Id    ) {
        this.Shipping_Type = Shipping_Type;
        this.Shipping_Id = Shipping_Id;
    }


    public String getShipping_type() {
        return Shipping_Type;
    }

    public void setShipping_type(String Shipping_Type) {
        this.Shipping_Type = Shipping_Type;
    }
    public int getShipping_id() {
        return Shipping_Id;
    }

    public void setShipping_id(int Shipping_Id) {
        this.Shipping_Id = Shipping_Id;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}