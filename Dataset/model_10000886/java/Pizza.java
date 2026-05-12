





import java.util.List;
import java.util.ArrayList;

public class Pizza  {

    private boolean isVegetarian;
    private float price;





    private Order order;


    public Pizza(
        boolean isVegetarian,        float price    ) {
        this.isVegetarian = isVegetarian;
        this.price = price;
    }


    public boolean getIsvegetarian() {
        return isVegetarian;
    }

    public void setIsvegetarian(boolean isVegetarian) {
        this.isVegetarian = isVegetarian;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}