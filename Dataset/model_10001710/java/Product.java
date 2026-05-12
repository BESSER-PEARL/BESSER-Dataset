





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String price;
    private String name;
    private String attribute;
    private String Category;





    private Order order;


    public Product(
        String price,        String name,        String attribute,        String Category    ) {
        this.price = price;
        this.name = name;
        this.attribute = attribute;
        this.Category = Category;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}