





import java.util.List;
import java.util.ArrayList;

public class Stock  {

    private String Items;





    private List<Product> products;


    public Stock(
        String Items    ) {
        this.Items = Items;
        this.products = new ArrayList<>();
    }

    public Stock(
        String Items        ArrayList<Product> products    ) {
        this.Items = Items;
        this.products = products;
    }

    public String getItems() {
        return Items;
    }

    public void setItems(String Items) {
        this.Items = Items;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}