





import java.util.List;
import java.util.ArrayList;

public class Appliacne  {

    private int price;
    private String name;





    private Product product;


    public Appliacne(
        int price,        String name    ) {
        this.price = price;
        this.name = name;
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

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}