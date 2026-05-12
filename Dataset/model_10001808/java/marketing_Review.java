





import java.util.List;
import java.util.ArrayList;

public class marketing_Review  {

    private None rating;
    private None user;
    private String description;
    private String id;
    private None product;



    public marketing_Review(
        None rating,        None user,        String description,        String id,        None product    ) {
        this.rating = rating;
        this.user = user;
        this.description = description;
        this.id = id;
        this.product = product;
    }


    public None getRating() {
        return rating;
    }

    public void setRating(None rating) {
        this.rating = rating;
    }
    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getProduct() {
        return product;
    }

    public void setProduct(None product) {
        this.product = product;
    }


}