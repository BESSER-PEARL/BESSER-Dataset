





import java.util.List;
import java.util.ArrayList;

public class ConfirmOrder  {

    private String OrderName;
    private String StoreName;
    private String Quantity;
    private String OrderPrice;



    public ConfirmOrder(
        String OrderName,        String StoreName,        String Quantity,        String OrderPrice    ) {
        this.OrderName = OrderName;
        this.StoreName = StoreName;
        this.Quantity = Quantity;
        this.OrderPrice = OrderPrice;
    }


    public String getOrdername() {
        return OrderName;
    }

    public void setOrdername(String OrderName) {
        this.OrderName = OrderName;
    }
    public String getStorename() {
        return StoreName;
    }

    public void setStorename(String StoreName) {
        this.StoreName = StoreName;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }
    public String getOrderprice() {
        return OrderPrice;
    }

    public void setOrderprice(String OrderPrice) {
        this.OrderPrice = OrderPrice;
    }


}