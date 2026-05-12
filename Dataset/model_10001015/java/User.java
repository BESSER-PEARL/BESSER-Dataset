





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int userId;





    private List<Product> products;


    public User(
        int userId    ) {
        this.userId = userId;
        this.products = new ArrayList<>();
    }

    public User(
        int userId        ArrayList<Product> products    ) {
        this.userId = userId;
        this.products = products;
    }

    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}