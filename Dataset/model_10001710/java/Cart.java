





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private String Id;
    private int items;





    private Product product;




    private Order order;


    public Cart(
        String Id,        int items    ) {
        this.Id = Id;
        this.items = items;
    }


    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public int getItems() {
        return items;
    }

    public void setItems(int items) {
        this.items = items;
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