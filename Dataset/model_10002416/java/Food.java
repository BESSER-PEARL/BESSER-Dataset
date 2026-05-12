





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private int type;
    private boolean prepared;
    private String description;
    private String food_Id;
    private boolean served;
    private String price;
    private String name;





    private List<Order> orders;


    public Food(
        int type,        boolean prepared,        String description,        String food_Id,        boolean served,        String price,        String name    ) {
        this.type = type;
        this.prepared = prepared;
        this.description = description;
        this.food_Id = food_Id;
        this.served = served;
        this.price = price;
        this.name = name;
        this.orders = new ArrayList<>();
    }

    public Food(
        int type,        boolean prepared,        String description,        String food_Id,        boolean served,        String price,        String name        ArrayList<Order> orders    ) {
        this.type = type;
        this.prepared = prepared;
        this.description = description;
        this.food_Id = food_Id;
        this.served = served;
        this.price = price;
        this.name = name;
        this.orders = orders;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFood_id() {
        return food_Id;
    }

    public void setFood_id(String food_Id) {
        this.food_Id = food_Id;
    }
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}