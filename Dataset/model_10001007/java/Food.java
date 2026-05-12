





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean prepared;
    private String food_Id;
    private int type;
    private boolean served;
    private String price;
    private String description;
    private String name;





    private List<Order> orders;


    public Food(
        boolean prepared,        String food_Id,        int type,        boolean served,        String price,        String description,        String name    ) {
        this.prepared = prepared;
        this.food_Id = food_Id;
        this.type = type;
        this.served = served;
        this.price = price;
        this.description = description;
        this.name = name;
        this.orders = new ArrayList<>();
    }

    public Food(
        boolean prepared,        String food_Id,        int type,        boolean served,        String price,        String description,        String name        ArrayList<Order> orders    ) {
        this.prepared = prepared;
        this.food_Id = food_Id;
        this.type = type;
        this.served = served;
        this.price = price;
        this.description = description;
        this.name = name;
        this.orders = orders;
    }

    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getFood_id() {
        return food_Id;
    }

    public void setFood_id(String food_Id) {
        this.food_Id = food_Id;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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