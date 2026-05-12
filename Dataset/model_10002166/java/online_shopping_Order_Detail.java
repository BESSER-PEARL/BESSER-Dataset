





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Order_Detail  {

    private String Product_ID;
    private None Product_Name;
    private String unit_Cost;
    private String Quantity;
    private String Subtotal;
    private String Order_ID;





    private online_shopping_Orders online_shopping_orders;




    private online_shopping_Product online_shopping_product;


    public online_shopping_Order_Detail(
        String Product_ID,        None Product_Name,        String unit_Cost,        String Quantity,        String Subtotal,        String Order_ID    ) {
        this.Product_ID = Product_ID;
        this.Product_Name = Product_Name;
        this.unit_Cost = unit_Cost;
        this.Quantity = Quantity;
        this.Subtotal = Subtotal;
        this.Order_ID = Order_ID;
    }


    public String getProduct_id() {
        return Product_ID;
    }

    public void setProduct_id(String Product_ID) {
        this.Product_ID = Product_ID;
    }
    public None getProduct_name() {
        return Product_Name;
    }

    public void setProduct_name(None Product_Name) {
        this.Product_Name = Product_Name;
    }
    public String getUnit_cost() {
        return unit_Cost;
    }

    public void setUnit_cost(String unit_Cost) {
        this.unit_Cost = unit_Cost;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getSubtotal() {
        return Subtotal;
    }

    public void setSubtotal(String Subtotal) {
        this.Subtotal = Subtotal;
    }
    public String getOrder_id() {
        return Order_ID;
    }

    public void setOrder_id(String Order_ID) {
        this.Order_ID = Order_ID;
    }

    public online_shopping_Orders getOnline_shopping_orders() {
        return online_shopping_orders;
    }

    public void setOnline_shopping_orders(online_shopping_Orders online_shopping_orders) {
        this.online_shopping_orders = online_shopping_orders;
    }
    public online_shopping_Product getOnline_shopping_product() {
        return online_shopping_product;
    }

    public void setOnline_shopping_product(online_shopping_Product online_shopping_product) {
        this.online_shopping_product = online_shopping_product;
    }

}