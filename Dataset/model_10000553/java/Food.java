





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean prepared;
    private float price;
    private String name;
    private boolean served;
    private String food_id;





    private Order order;


    public Food(
        boolean prepared,        float price,        String name,        boolean served,        String food_id    ) {
        this.prepared = prepared;
        this.price = price;
        this.name = name;
        this.served = served;
        this.food_id = food_id;
    }


    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
    }
    public String getFood_id() {
        return food_id;
    }

    public void setFood_id(String food_id) {
        this.food_id = food_id;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}