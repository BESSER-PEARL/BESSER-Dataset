





import java.util.List;
import java.util.ArrayList;

public class Warehouse  {

    private String location;
    private String name;





    private List<Product> products;


    public Warehouse(
        String location,        String name    ) {
        this.location = location;
        this.name = name;
        this.products = new ArrayList<>();
    }

    public Warehouse(
        String location,        String name        ArrayList<Product> products    ) {
        this.location = location;
        this.name = name;
        this.products = products;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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