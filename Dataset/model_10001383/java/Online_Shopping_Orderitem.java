





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Orderitem  {

    private int Quantity;
    private String ProductID;
    private String Sub_Total;





    private Online_Shopping_Order online_shopping_order;


    public Online_Shopping_Orderitem(
        int Quantity,        String ProductID,        String Sub_Total    ) {
        this.Quantity = Quantity;
        this.ProductID = ProductID;
        this.Sub_Total = Sub_Total;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public String getProductid() {
        return ProductID;
    }

    public void setProductid(String ProductID) {
        this.ProductID = ProductID;
    }
    public String getSub_total() {
        return Sub_Total;
    }

    public void setSub_total(String Sub_Total) {
        this.Sub_Total = Sub_Total;
    }

    public Online_Shopping_Order getOnline_shopping_order() {
        return online_shopping_order;
    }

    public void setOnline_shopping_order(Online_Shopping_Order online_shopping_order) {
        this.online_shopping_order = online_shopping_order;
    }

}