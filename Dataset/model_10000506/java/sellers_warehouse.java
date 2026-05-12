





import java.util.List;
import java.util.ArrayList;

public class sellers_warehouse  {

    private String location;
    private String database;





    private List<Product> products;


    public sellers_warehouse(
        String location,        String database    ) {
        this.location = location;
        this.database = database;
        this.products = new ArrayList<>();
    }

    public sellers_warehouse(
        String location,        String database        ArrayList<Product> products    ) {
        this.location = location;
        this.database = database;
        this.products = products;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}