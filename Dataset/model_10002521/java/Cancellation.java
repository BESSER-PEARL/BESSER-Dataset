





import java.util.List;
import java.util.ArrayList;

public class Cancellation  {

    private String productID;
    private String amount;
    private String customerID;





    private Product product;


    public Cancellation(
        String productID,        String amount,        String customerID    ) {
        this.productID = productID;
        this.amount = amount;
        this.customerID = customerID;
    }


    public String getProductid() {
        return productID;
    }

    public void setProductid(String productID) {
        this.productID = productID;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getCustomerid() {
        return customerID;
    }

    public void setCustomerid(String customerID) {
        this.customerID = customerID;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}