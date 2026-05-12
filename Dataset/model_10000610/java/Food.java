





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String name;
    private String description;
    private String food_Id;
    private boolean served;
    private boolean prepared;
    private String price;
    private int type;





    private List<Order> orders;


    public Food(
        String name,        String description,        String food_Id,        boolean served,        boolean prepared,        String price,        int type    ) {
        this.name = name;
        this.description = description;
        this.food_Id = food_Id;
        this.served = served;
        this.prepared = prepared;
        this.price = price;
        this.type = type;
        this.orders = new ArrayList<>();
    }

    public Food(
        String name,        String description,        String food_Id,        boolean served,        boolean prepared,        String price,        int type        ArrayList<Order> orders    ) {
        this.name = name;
        this.description = description;
        this.food_Id = food_Id;
        this.served = served;
        this.prepared = prepared;
        this.price = price;
        this.type = type;
        this.orders = orders;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
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