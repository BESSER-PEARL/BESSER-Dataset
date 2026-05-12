





import java.util.List;
import java.util.ArrayList;

public class Retailer_Cart  {

    private float quantity___product;
    private None product;
    private int userID;





    private Retailer retailer;


    public Retailer_Cart(
        float quantity___product,        None product,        int userID    ) {
        this.quantity___product = quantity___product;
        this.product = product;
        this.userID = userID;
    }


    public float getQuantity___product() {
        return quantity___product;
    }

    public void setQuantity___product(float quantity___product) {
        this.quantity___product = quantity___product;
    }
    public None getProduct() {
        return product;
    }

    public void setProduct(None product) {
        this.product = product;
    }
    public int getUserid() {
        return userID;
    }

    public void setUserid(int userID) {
        this.userID = userID;
    }

    public Retailer getRetailer() {
        return retailer;
    }

    public void setRetailer(Retailer retailer) {
        this.retailer = retailer;
    }

}