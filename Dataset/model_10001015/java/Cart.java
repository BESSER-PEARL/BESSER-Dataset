





import java.util.List;
import java.util.ArrayList;

public class Cart  {






    private Customer customer;




    private ProductListHelper productlisthelper;




    private Product product;


    public Cart(
    ) {
    }



    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public ProductListHelper getProductlisthelper() {
        return productlisthelper;
    }

    public void setProductlisthelper(ProductListHelper productlisthelper) {
        this.productlisthelper = productlisthelper;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}