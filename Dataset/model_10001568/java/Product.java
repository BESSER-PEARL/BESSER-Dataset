





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private int price;
    private String name;
    private int quantity;
    private int ProductID;



    public Product(
        String description,        int price,        String name,        int quantity,        int ProductID    ) {
        this.description = description;
        this.price = price;
        this.name = name;
        this.quantity = quantity;
        this.ProductID = ProductID;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }


}