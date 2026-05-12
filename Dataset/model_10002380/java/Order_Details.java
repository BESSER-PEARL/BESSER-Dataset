





import java.util.List;
import java.util.ArrayList;

public class Order_Details  {

    private int Product_Id;
    private int Order_Id;
    private String Sub_Total;
    private String Product_Name;
    private int Quantity;
    private String Unicast;





    private Orders orders;


    public Order_Details(
        int Product_Id,        int Order_Id,        String Sub_Total,        String Product_Name,        int Quantity,        String Unicast    ) {
        this.Product_Id = Product_Id;
        this.Order_Id = Order_Id;
        this.Sub_Total = Sub_Total;
        this.Product_Name = Product_Name;
        this.Quantity = Quantity;
        this.Unicast = Unicast;
    }


    public int getProduct_id() {
        return Product_Id;
    }

    public void setProduct_id(int Product_Id) {
        this.Product_Id = Product_Id;
    }
    public int getOrder_id() {
        return Order_Id;
    }

    public void setOrder_id(int Order_Id) {
        this.Order_Id = Order_Id;
    }
    public String getSub_total() {
        return Sub_Total;
    }

    public void setSub_total(String Sub_Total) {
        this.Sub_Total = Sub_Total;
    }
    public String getProduct_name() {
        return Product_Name;
    }

    public void setProduct_name(String Product_Name) {
        this.Product_Name = Product_Name;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public String getUnicast() {
        return Unicast;
    }

    public void setUnicast(String Unicast) {
        this.Unicast = Unicast;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}