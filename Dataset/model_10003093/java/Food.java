





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean prepared;
    private String description;
    private int type;
    private String food_Id;
    private String name;
    private boolean served;
    private String price;





    private List<Order> orders;


    public Food(
        boolean prepared,        String description,        int type,        String food_Id,        String name,        boolean served,        String price    ) {
        this.prepared = prepared;
        this.description = description;
        this.type = type;
        this.food_Id = food_Id;
        this.name = name;
        this.served = served;
        this.price = price;
        this.orders = new ArrayList<>();
    }

    public Food(
        boolean prepared,        String description,        int type,        String food_Id,        String name,        boolean served,        String price        ArrayList<Order> orders    ) {
        this.prepared = prepared;
        this.description = description;
        this.type = type;
        this.food_Id = food_Id;
        this.name = name;
        this.served = served;
        this.price = price;
        this.orders = orders;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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