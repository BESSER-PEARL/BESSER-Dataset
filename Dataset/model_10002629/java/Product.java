





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private String name;





    private List<Product_View> product_views;


    public Product(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.product_views = new ArrayList<>();
    }

    public Product(
        String description,        String name        ArrayList<Product_View> product_views    ) {
        this.description = description;
        this.name = name;
        this.product_views = product_views;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Product_View> getProduct_views() {
        return product_views;
    }

    public void addProduct_view(Product_view product_view) {
        this.product_views.add(product_view);
    }

}