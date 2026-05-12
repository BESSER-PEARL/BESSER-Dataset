





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String photoPath;
    private int id;
    private String name;





    private List<Product> products;


    public Category(
        String photoPath,        int id,        String name    ) {
        this.photoPath = photoPath;
        this.id = id;
        this.name = name;
        this.products = new ArrayList<>();
    }

    public Category(
        String photoPath,        int id,        String name        ArrayList<Product> products    ) {
        this.photoPath = photoPath;
        this.id = id;
        this.name = name;
        this.products = products;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}