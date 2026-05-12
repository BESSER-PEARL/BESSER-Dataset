





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String food_Id;
    private boolean prepared;
    private boolean served;
    private String name;
    private int type;
    private String description;
    private String price;





    private List<Order> orders;


    public Food(
        String food_Id,        boolean prepared,        boolean served,        String name,        int type,        String description,        String price    ) {
        this.food_Id = food_Id;
        this.prepared = prepared;
        this.served = served;
        this.name = name;
        this.type = type;
        this.description = description;
        this.price = price;
        this.orders = new ArrayList<>();
    }

    public Food(
        String food_Id,        boolean prepared,        boolean served,        String name,        int type,        String description,        String price        ArrayList<Order> orders    ) {
        this.food_Id = food_Id;
        this.prepared = prepared;
        this.served = served;
        this.name = name;
        this.type = type;
        this.description = description;
        this.price = price;
        this.orders = orders;
    }

    public String getFood_id() {
        return food_Id;
    }

    public void setFood_id(String food_Id) {
        this.food_Id = food_Id;
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
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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