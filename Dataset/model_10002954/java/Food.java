





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private float price;
    private boolean prepared;
    private String name;
    private String food_id;
    private boolean served;





    private Order order;


    public Food(
        float price,        boolean prepared,        String name,        String food_id,        boolean served    ) {
        this.price = price;
        this.prepared = prepared;
        this.name = name;
        this.food_id = food_id;
        this.served = served;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}