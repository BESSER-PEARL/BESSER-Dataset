





import java.util.List;
import java.util.ArrayList;

public class Seller  {

    private String sellerId;
    private String rating;
    private String name;





    private Product product;


    public Seller(
        String sellerId,        String rating,        String name    ) {
        this.sellerId = sellerId;
        this.rating = rating;
        this.name = name;
    }


    public String getSellerid() {
        return sellerId;
    }

    public void setSellerid(String sellerId) {
        this.sellerId = sellerId;
    }
    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}