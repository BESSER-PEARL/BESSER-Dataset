





import java.util.List;
import java.util.ArrayList;

public class marketing_Review  {

    private String description;
    private None user;
    private None product;
    private String rating;
    private String id;



    public marketing_Review(
        String description,        None user,        None product,        String rating,        String id    ) {
        this.description = description;
        this.user = user;
        this.product = product;
        this.rating = rating;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }
    public None getProduct() {
        return product;
    }

    public void setProduct(None product) {
        this.product = product;
    }
    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}