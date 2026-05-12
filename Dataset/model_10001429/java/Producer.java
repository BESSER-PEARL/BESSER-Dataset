





import java.util.List;
import java.util.ArrayList;

public class Producer  {

    private String country;
    private String name;
    private int u_id;





    private List<Product> products;


    public Producer(
        String country,        String name,        int u_id    ) {
        this.country = country;
        this.name = name;
        this.u_id = u_id;
        this.products = new ArrayList<>();
    }

    public Producer(
        String country,        String name,        int u_id        ArrayList<Product> products    ) {
        this.country = country;
        this.name = name;
        this.u_id = u_id;
        this.products = products;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getU_id() {
        return u_id;
    }

    public void setU_id(int u_id) {
        this.u_id = u_id;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}