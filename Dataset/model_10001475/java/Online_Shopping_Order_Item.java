





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Order_Item  {

    private String Product_ID;
    private String SubTotal;
    private int Quantity;



    public Online_Shopping_Order_Item(
        String Product_ID,        String SubTotal,        int Quantity    ) {
        this.Product_ID = Product_ID;
        this.SubTotal = SubTotal;
        this.Quantity = Quantity;
    }


    public String getProduct_id() {
        return Product_ID;
    }

    public void setProduct_id(String Product_ID) {
        this.Product_ID = Product_ID;
    }
    public String getSubtotal() {
        return SubTotal;
    }

    public void setSubtotal(String SubTotal) {
        this.SubTotal = SubTotal;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }


}