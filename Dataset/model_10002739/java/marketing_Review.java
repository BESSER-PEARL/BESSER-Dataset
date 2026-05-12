





import java.util.List;
import java.util.ArrayList;

public class marketing_Review  {

    private String id;
    private None product;
    private None user;
    private String description;
    private None rating;



    public marketing_Review(
        String id,        None product,        None user,        String description,        None rating    ) {
        this.id = id;
        this.product = product;
        this.user = user;
        this.description = description;
        this.rating = rating;
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
    public None getRating() {
        return rating;
    }

    public void setRating(None rating) {
        this.rating = rating;
    }


}