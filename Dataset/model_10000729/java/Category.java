





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String name;
    private String photoPath;
    private int id;





    private List<Product> products;


    public Category(
        String name,        String photoPath,        int id    ) {
        this.name = name;
        this.photoPath = photoPath;
        this.id = id;
        this.products = new ArrayList<>();
    }

    public Category(
        String name,        String photoPath,        int id        ArrayList<Product> products    ) {
        this.name = name;
        this.photoPath = photoPath;
        this.id = id;
        this.products = products;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhotopath() {
        return photoPath;
    }

    public void setPhotopath(String photoPath) {
        this.photoPath = photoPath;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}