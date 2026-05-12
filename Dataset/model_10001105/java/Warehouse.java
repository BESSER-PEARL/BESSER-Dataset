





import java.util.List;
import java.util.ArrayList;

public class Warehouse  {

    private String database;
    private String location;





    private List<Product> products;


    public Warehouse(
        String database,        String location    ) {
        this.database = database;
        this.location = location;
        this.products = new ArrayList<>();
    }

    public Warehouse(
        String database,        String location        ArrayList<Product> products    ) {
        this.database = database;
        this.location = location;
        this.products = products;
    }

    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}