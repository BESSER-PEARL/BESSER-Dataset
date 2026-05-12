





import java.util.List;
import java.util.ArrayList;

public class Category  {

    private String name;
    private int id;
    private String photoPath;





    private List<Product> products;


    public Category(
        String name,        int id,        String photoPath    ) {
        this.name = name;
        this.id = id;
        this.photoPath = photoPath;
        this.products = new ArrayList<>();
    }

    public Category(
        String name,        int id,        String photoPath        ArrayList<Product> products    ) {
        this.name = name;
        this.id = id;
        this.photoPath = photoPath;
        this.products = products;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPhotopath() {
        return photoPath;
    }

    public void setPhotopath(String photoPath) {
        this.photoPath = photoPath;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}