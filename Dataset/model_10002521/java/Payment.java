





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String productID;
    private String customerId;
    private int amount;





    private Shopping_Cart shopping_cart;


    public Payment(
        String productID,        String customerId,        int amount    ) {
        this.productID = productID;
        this.customerId = customerId;
        this.amount = amount;
    }


    public String getProductid() {
        return productID;
    }

    public void setProductid(String productID) {
        this.productID = productID;
    }
    public String getCustomerid() {
        return customerId;
    }

    public void setCustomerid(String customerId) {
        this.customerId = customerId;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Shopping_Cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_Cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

}