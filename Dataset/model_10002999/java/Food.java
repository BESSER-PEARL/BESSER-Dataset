





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String name;
    private int type;
    private boolean prepared;
    private boolean served;
    private String food_Id;
    private String description;
    private String price;





    private List<Order> orders;


    public Food(
        String name,        int type,        boolean prepared,        boolean served,        String food_Id,        String description,        String price    ) {
        this.name = name;
        this.type = type;
        this.prepared = prepared;
        this.served = served;
        this.food_Id = food_Id;
        this.description = description;
        this.price = price;
        this.orders = new ArrayList<>();
    }

    public Food(
        String name,        int type,        boolean prepared,        boolean served,        String food_Id,        String description,        String price        ArrayList<Order> orders    ) {
        this.name = name;
        this.type = type;
        this.prepared = prepared;
        this.served = served;
        this.food_Id = food_Id;
        this.description = description;
        this.price = price;
        this.orders = orders;
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