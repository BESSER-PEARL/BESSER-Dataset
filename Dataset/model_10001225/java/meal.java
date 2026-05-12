





import java.util.List;
import java.util.ArrayList;

public class meal  {

    private float price;
    private boolean served;
    private String meal_id;
    private String name;
    private boolean prepared;





    private Order order;


    public meal(
        float price,        boolean served,        String meal_id,        String name,        boolean prepared    ) {
        this.price = price;
        this.served = served;
        this.meal_id = meal_id;
        this.name = name;
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
    public String getMeal_id() {
        return meal_id;
    }

    public void setMeal_id(String meal_id) {
        this.meal_id = meal_id;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}