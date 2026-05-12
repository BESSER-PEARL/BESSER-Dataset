





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private String ProductPurchased;





    private ClientAccount clientaccount;




    private Product product;




    private Order order;


    public Shopping_Cart(
        String ProductPurchased    ) {
        this.ProductPurchased = ProductPurchased;
    }


    public String getProductpurchased() {
        return ProductPurchased;
    }

    public void setProductpurchased(String ProductPurchased) {
        this.ProductPurchased = ProductPurchased;
    }

    public ClientAccount getClientaccount() {
        return clientaccount;
    }

    public void setClientaccount(ClientAccount clientaccount) {
        this.clientaccount = clientaccount;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}