





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String food_id;
    private String name;
    private boolean prepared;
    private float price;
    private boolean served;





    private Order order;


    public Food(
        String food_id,        String name,        boolean prepared,        float price,        boolean served    ) {
        this.food_id = food_id;
        this.name = name;
        this.prepared = prepared;
        this.price = price;
        this.served = served;
    }


    public String getFood_id() {
        return food_id;
    }

    public void setFood_id(String food_id) {
        this.food_id = food_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}