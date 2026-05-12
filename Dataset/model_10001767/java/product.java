





import java.util.List;
import java.util.ArrayList;

public class product  {

    private int productId;
    private String image;
    private int price;
    private String name;
    private String description;





    private cartitem cartitem;


    public product(
        int productId,        String image,        int price,        String name,        String description    ) {
        this.productId = productId;
        this.image = image;
        this.price = price;
        this.name = name;
        this.description = description;
    }


    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public cartitem getCartitem() {
        return cartitem;
    }

    public void setCartitem(cartitem cartitem) {
        this.cartitem = cartitem;
    }

}