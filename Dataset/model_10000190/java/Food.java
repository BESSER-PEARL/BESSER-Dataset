





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private float price;
    private String food_id;
    private boolean prepared;
    private boolean served;
    private String name;





    private Order order;


    public Food(
        float price,        String food_id,        boolean prepared,        boolean served,        String name    ) {
        this.price = price;
        this.food_id = food_id;
        this.prepared = prepared;
        this.served = served;
        this.name = name;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
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
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}