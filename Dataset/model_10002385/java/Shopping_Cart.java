





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private None customerId;
    private String price;
    private int orderId;



    public Shopping_Cart(
        None customerId,        String price,        int orderId    ) {
        this.customerId = customerId;
        this.price = price;
        this.orderId = orderId;
    }


    public None getCustomerid() {
        return customerId;
    }

    public void setCustomerid(None customerId) {
        this.customerId = customerId;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }


}