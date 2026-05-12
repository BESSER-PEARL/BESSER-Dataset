





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String name;
    private boolean prepared;
    private int type;
    private String food_Id;
    private String description;
    private boolean served;
    private String price;





    private List<Order> orders;


    public Food(
        String name,        boolean prepared,        int type,        String food_Id,        String description,        boolean served,        String price    ) {
        this.name = name;
        this.prepared = prepared;
        this.type = type;
        this.food_Id = food_Id;
        this.description = description;
        this.served = served;
        this.price = price;
        this.orders = new ArrayList<>();
    }

    public Food(
        String name,        boolean prepared,        int type,        String food_Id,        String description,        boolean served,        String price        ArrayList<Order> orders    ) {
        this.name = name;
        this.prepared = prepared;
        this.type = type;
        this.food_Id = food_Id;
        this.description = description;
        this.served = served;
        this.price = price;
        this.orders = orders;
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
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getFood_id() {
        return food_Id;
    }

    public void setFood_id(String food_Id) {
        this.food_Id = food_Id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}