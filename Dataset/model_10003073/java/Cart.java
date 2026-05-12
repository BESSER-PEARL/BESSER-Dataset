





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private None Product;





    private List<Product> products;


    public Cart(
        None Product    ) {
        this.Product = Product;
        this.products = new ArrayList<>();
    }

    public Cart(
        None Product        ArrayList<Product> products    ) {
        this.Product = Product;
        this.products = products;
    }

    public None getProduct() {
        return Product;
    }

    public void setProduct(None Product) {
        this.Product = Product;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}