





import java.util.List;
import java.util.ArrayList;

public class ProductGroupProduct  {

    private None Product;
    private None ProductGroup;
    private int id;
    private int weight;





    private Product product;




    private ProductGroup productgroup;


    public ProductGroupProduct(
        None Product,        None ProductGroup,        int id,        int weight    ) {
        this.Product = Product;
        this.ProductGroup = ProductGroup;
        this.id = id;
        this.weight = weight;
    }


    public None getProduct() {
        return Product;
    }

    public void setProduct(None Product) {
        this.Product = Product;
    }
    public None getProductgroup() {
        return ProductGroup;
    }

    public void setProductgroup(None ProductGroup) {
        this.ProductGroup = ProductGroup;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
    public ProductGroup getProductgroup() {
        return productgroup;
    }

    public void setProductgroup(ProductGroup productgroup) {
        this.productgroup = productgroup;
    }

}