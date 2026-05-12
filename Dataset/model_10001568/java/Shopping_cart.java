





import java.util.List;
import java.util.ArrayList;

public class Shopping_cart  {

    private String Products;





    private List<Product> products;


    public Shopping_cart(
        String Products    ) {
        this.Products = Products;
        this.products = new ArrayList<>();
    }

    public Shopping_cart(
        String Products        ArrayList<Product> products    ) {
        this.Products = Products;
        this.products = products;
    }

    public String getProducts() {
        return Products;
    }

    public void setProducts(String Products) {
        this.Products = Products;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}