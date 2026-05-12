





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int rating;
    private String description;
    private String productName;
    private int productId;
    private int price;
    private String image;
    private None sellerInfo;



    public Product(
        int rating,        String description,        String productName,        int productId,        int price,        String image,        None sellerInfo    ) {
        this.rating = rating;
        this.description = description;
        this.productName = productName;
        this.productId = productId;
        this.price = price;
        this.image = image;
        this.sellerInfo = sellerInfo;
    }


    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public None getSellerinfo() {
        return sellerInfo;
    }

    public void setSellerinfo(None sellerInfo) {
        this.sellerInfo = sellerInfo;
    }


}