





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String food_id;
    private String name;
    private float price;
    private boolean prepared;
    private boolean served;





    private Order order;


    public Food(
        String food_id,        String name,        float price,        boolean prepared,        boolean served    ) {
        this.food_id = food_id;
        this.name = name;
        this.price = price;
        this.prepared = prepared;
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
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}