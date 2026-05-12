





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String description;
    private String name;
    private int type;
    private String price;
    private String food_Id;
    private boolean prepared;
    private boolean served;





    private List<Order> orders;


    public Food(
        String description,        String name,        int type,        String price,        String food_Id,        boolean prepared,        boolean served    ) {
        this.description = description;
        this.name = name;
        this.type = type;
        this.price = price;
        this.food_Id = food_Id;
        this.prepared = prepared;
        this.served = served;
        this.orders = new ArrayList<>();
    }

    public Food(
        String description,        String name,        int type,        String price,        String food_Id,        boolean prepared,        boolean served        ArrayList<Order> orders    ) {
        this.description = description;
        this.name = name;
        this.type = type;
        this.price = price;
        this.food_Id = food_Id;
        this.prepared = prepared;
        this.served = served;
        this.orders = orders;
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
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}