





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean served;
    private String food_id;
    private boolean prepared;
    private String name;
    private float price;





    private Order order;


    public Food(
        boolean served,        String food_id,        boolean prepared,        String name,        float price    ) {
        this.served = served;
        this.food_id = food_id;
        this.prepared = prepared;
        this.name = name;
        this.price = price;
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
    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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