





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean prepared;
    private boolean served;
    private String food_Id;
    private String name;
    private String price;
    private String description;
    private int type;





    private List<Order> orders;


    public Food(
        boolean prepared,        boolean served,        String food_Id,        String name,        String price,        String description,        int type    ) {
        this.prepared = prepared;
        this.served = served;
        this.food_Id = food_Id;
        this.name = name;
        this.price = price;
        this.description = description;
        this.type = type;
        this.orders = new ArrayList<>();
    }

    public Food(
        boolean prepared,        boolean served,        String food_Id,        String name,        String price,        String description,        int type        ArrayList<Order> orders    ) {
        this.prepared = prepared;
        this.served = served;
        this.food_Id = food_Id;
        this.name = name;
        this.price = price;
        this.description = description;
        this.type = type;
        this.orders = orders;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}