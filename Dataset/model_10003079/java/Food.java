





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private String food_Id;
    private boolean prepared;
    private String price;
    private String description;
    private int type;
    private String name;
    private boolean served;





    private List<Order> orders;


    public Food(
        String food_Id,        boolean prepared,        String price,        String description,        int type,        String name,        boolean served    ) {
        this.food_Id = food_Id;
        this.prepared = prepared;
        this.price = price;
        this.description = description;
        this.type = type;
        this.name = name;
        this.served = served;
        this.orders = new ArrayList<>();
    }

    public Food(
        String food_Id,        boolean prepared,        String price,        String description,        int type,        String name,        boolean served        ArrayList<Order> orders    ) {
        this.food_Id = food_Id;
        this.prepared = prepared;
        this.price = price;
        this.description = description;
        this.type = type;
        this.name = name;
        this.served = served;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}