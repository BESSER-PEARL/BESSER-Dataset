





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean prepared;
    private String food_id;
    private boolean served;
    private float price;
    private String name;





    private Order order;


    public Food(
        boolean prepared,        String food_id,        boolean served,        float price,        String name    ) {
        this.prepared = prepared;
        this.food_id = food_id;
        this.served = served;
        this.price = price;
        this.name = name;
    }


    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getFood_id() {
        return food_id;
    }

    public void setFood_id(String food_id) {
        this.food_id = food_id;
    }
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}